# Task 1 (Intermediate): Web Scraper
import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

print("Scraped Quotes:")
for i in range(min(5, len(quotes))):
    print(f"Quote {i+1}: {quotes[i].text}")
    print(f"Author: {authors[i].text}")
    print("-" * 50)

#Requirements 
#pip install requests beautifulsoup4
