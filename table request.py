import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_IBA_official_cocktails"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html5lib")

results = soup.find_all("dl")

data = []
for result in results:
    mw_headline = result.find_previous_sibling('span', {'class': 'mw-headline'})
    dt_elements = result.find_all('dt')
    dd_elements = result.find_all('dd')
    for dt, dd in zip(dt_elements, dd_elements):
        row = {
            'mw-headline': mw_headline.text if mw_headline else '',
            'dt_title': dt.text,
            'dt_href': dt.a.get('href', '') if dt.a else '',
            'dd_text': dd.text if dd else ''
        }
        data.append(row)

df = pd.DataFrame(data)

# Write DataFrame to CSV file
df.to_csv('output.csv', index=False)