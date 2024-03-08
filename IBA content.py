import requests
from bs4 import BeautifulSoup

URL = "https://iba-world.com/alexander/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# cocktail = soup.find_all("h1", class_="entry-title")

# Print all the text in the page
print(soup)

