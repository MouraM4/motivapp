
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Define the Selenium Configurations
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-application-cache")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

# Create a list of urls for the site that we are scraping motivational messages
url = 'https://www.pensador.com/frases_motivacionais/'
url_list = [ f'{url}{i}' for i in range (1,11,1)]
message_list_all = []

# Get all message for each url
for url in url_list:
    # Do a GET request in the url
    driver.get(url)
    print(f"Scraping the page: {url}")
    # Get all the elements that has the messages
    message_list_elements = driver.find_elements_by_xpath("//*[@class='frase fr']")
    # Extract all messages text from it's elements and create a list
    message_list = [ message.text for message in message_list_elements]
    # Concatenate the list of messages from a specific url with general list
    message_list_all = message_list_all + message_list
    print("Added Messages!")

print(f"Total de mensagens adicionadas: {len(message_list_all)}")

# Saving the list as csv
messages_df = pd.DataFrame()
messages_df['messages'] = message_list_all
messages_df.to_csv("motivational_messages.csv", header=False)