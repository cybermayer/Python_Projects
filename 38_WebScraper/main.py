from bs4 import BeautifulSoup
import requests

#Fetch the webpage's data from Hacker News
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text  

soup = BeautifulSoup(yc_web_page, "html.parser")

#Find all <a> elements with class "storylink", which contain article titles and links
articles = soup.find_all(name="a", class_="storylink")

#Initialize lists for contents and links
article_texts = []
article_links = []

#Iterate through each <a> element, extract and process the article text and link
for article_tag in articles:
    text = article_tag.getText()  
    article_texts.append(text)  
    link = article_tag.get("href")
    article_links.append(link)

#Extract the upvote scores of each article
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

#Find the index of the article with the highest number of upvotes
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

#Print the title and link of the article with the highest upvotes
print(article_texts[largest_index])
print(article_links[largest_index])













