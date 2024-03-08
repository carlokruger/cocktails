from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML content
with open('wiki_IBA_Cockails.html', 'r') as f:
    content = f.read()

# Parse the HTML
soup = BeautifulSoup(content, 'html.parser')

# Find all 'dl' elements
dl_elements = soup.find_all('dl')

data = []
for dl in dl_elements:
    dt_elements = dl.find_all('dt')
    dd_elements = dl.find_all('dd')
    
    # Handle 'dt' tags
    for dt in dt_elements:
        row = {'dt': dt.get_text(strip=True)}
        data.append(row)
    
    # Handle 'dd' tags
    for i, dd in enumerate(dd_elements):
        if i < len(data):
            # Add the 'dd' tag as a new column in the corresponding row
            data[i]['dd' + str(i+1)] = dd.get_text(strip=True)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write DataFrame to CSV file
df.to_csv('output3.csv', index=False)