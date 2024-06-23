from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

#Define headers with user-agent and language preferences
header = {
    "User-Agent": "YOUR USER AGENT",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

#Send a GET request to fetch the Zillow webpage with specific search parameters
response = requests.get(
    "https://www.zillow.com/manhattan-new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.877483%2C%22south%22%3A40.683935%2C%22east%22%3A-73.910408%2C%22west%22%3A-74.047237%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12530%2C%22regionType%22%3A17%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22usersSearchTerm%22%3A%22Manhattan%20New%20York%20NY%22%7D",
    headers=header)

#Fetching web-data and create the BS object
data = response.text  
soup = BeautifulSoup(data, "html.parser")

#Select all elements containing property links
all_link_elements = soup.select(".list-card-top a")
all_links = []

#Iterate through each link element and extract the href attribute
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")  # Append full URL if href is relative
    else:
        all_links.append(href)  # Append URL as is if href is already absolute

#Select all elements containing property addresses
all_address_elements = soup.select(".list-card-info address")

#Extract the text of each address element and store in a list
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

#Select all elements containing property prices
all_price_elements = soup.select(".list-card-heading")
all_prices = []

#Iterate through each price element and extract the information
for element in all_price_elements:
    try:
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)

#Setting path for the Chrome WebDriver executable
chrome_driver_path = YOUR_PATH_HERE
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#Iterate through each property and fill out a Google Form
for n in range(len(all_links)):
    driver.get(URL_TO_YOUR_GOOGLE_FORM)

    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
