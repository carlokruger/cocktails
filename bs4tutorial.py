import requests
import html5lib
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd


URL = "https://en.wikipedia.org/wiki/List_of_IBA_official_cocktails"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html5lib")

results = soup.find_all("dl")

data = []
for result in results:
    row = {}
    for tag in result.find_all(['dt', 'dd']):
        row[tag.name] = tag.text
    data.append(row)

df = pd.DataFrame(data)

# Write DataFrame to CSV file
df.to_csv('output.csv', index=False)