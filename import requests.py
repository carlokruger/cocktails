import requests
from bs4 import BeautifulSoup
import pandas as pd

url_list = [
"https://en.wikipedia.org/wiki/Alexander_(cocktail)",
"https://en.wikipedia.org/wiki/Americano_(cocktail)",
"https://en.wikipedia.org/wiki/Angel_face_(cocktail)",
"https://en.wikipedia.org/wiki/Aviation_(cocktail)",
"https://en.wikipedia.org/wiki/Between_the_sheets_(cocktail)",
"https://en.wikipedia.org/wiki/Boulevardier_(cocktail)",
"https://en.wikipedia.org/wiki/Brandy_crusta",
"https://en.wikipedia.org/wiki/Casino_(cocktail)",
"https://en.wikipedia.org/wiki/Clover_Club_cocktail",
"https://en.wikipedia.org/wiki/Daiquiri",
"https://en.wikipedia.org/wiki/Martini_(cocktail)",
"https://en.wikipedia.org/wiki/Gin_fizz",
"https://en.wikipedia.org/wiki/Hanky_panky_(cocktail)",
"https://en.wikipedia.org/wiki/John_Collins_(cocktail)",
"https://en.wikipedia.org/wiki/Last_word_(cocktail)",
"https://en.wikipedia.org/wiki/Manhattan_(cocktail)",
"https://en.wikipedia.org/wiki/Martinez_(cocktail)",
"https://en.wikipedia.org/wiki/Mary_Pickford_(cocktail)",
"https://en.wikipedia.org/wiki/Monkey_gland_(cocktail)",
"https://en.wikipedia.org/wiki/Negroni",
"https://en.wikipedia.org/wiki/Old_fashioned_(cocktail)",
"https://en.wikipedia.org/wiki/Paradise_(cocktail)",
"https://en.wikipedia.org/wiki/Planter%27s_punch",
"https://en.wikipedia.org/wiki/Porto_flip",
"https://en.wikipedia.org/wiki/Ramos_fizz",
"https://en.wikipedia.org/wiki/Rusty_nail_(cocktail)",
"https://en.wikipedia.org/wiki/Sazerac",
"https://en.wikipedia.org/wiki/Sidecar_(cocktail)",
"https://en.wikipedia.org/wiki/Stinger_(cocktail)",
"https://en.wikipedia.org/wiki/Tuxedo_(cocktail)",
"https://en.wikipedia.org/wiki/Vieux_Carr%C3%A9_(cocktail)",
"https://en.wikipedia.org/wiki/Whiskey_sour",
"https://en.wikipedia.org/wiki/White_lady_(cocktail)",
"https://en.wikipedia.org/wiki/Bellini_(cocktail)",
"https://en.wikipedia.org/wiki/Black_Russian",
"https://en.wikipedia.org/wiki/Bloody_Mary_(cocktail)",
"https://en.wikipedia.org/wiki/Caipirinha",
"https://en.wikipedia.org/wiki/Champagne_cocktail",
"https://en.wikipedia.org/wiki/Corpse_reviver#Corpse_reviver_#2_and_#2A",
"https://en.wikipedia.org/wiki/Cosmopolitan_(cocktail)",
"https://en.wikipedia.org/wiki/Rum_and_Coke",
"https://en.wikipedia.org/wiki/French_75_(cocktail)",
"https://en.wikipedia.org/wiki/French_Connection_(cocktail)",
"https://en.wikipedia.org/wiki/Golden_dream_(cocktail)",
"https://en.wikipedia.org/wiki/Grasshopper_(cocktail)",
"https://en.wikipedia.org/wiki/Hemingway_special",
"https://en.wikipedia.org/wiki/Horse%27s_neck",
"https://en.wikipedia.org/wiki/Irish_coffee",
"https://en.wikipedia.org/wiki/Kir_(cocktail)",
"https://en.wikipedia.org/wiki/Long_Island_iced_tea",
"https://en.wikipedia.org/wiki/Mai_Tai",
"https://en.wikipedia.org/wiki/Margarita",
"https://en.wikipedia.org/wiki/Mimosa_(cocktail)",
"https://en.wikipedia.org/wiki/Mint_julep",
"https://en.wikipedia.org/wiki/Mojito",
"https://en.wikipedia.org/wiki/Moscow_mule",
"https://en.wikipedia.org/wiki/Pi%C3%B1a_colada",
"https://en.wikipedia.org/wiki/Pisco_sour",
"https://en.wikipedia.org/wiki/Sea_breeze_(cocktail)",
"https://en.wikipedia.org/wiki/Sex_on_the_beach",
"https://en.wikipedia.org/wiki/Singapore_sling",
"https://en.wikipedia.org/wiki/Tequila_sunrise",
"https://en.wikipedia.org/wiki/Vesper_(cocktail)",
"https://en.wikipedia.org/wiki/Zombie_(cocktail)",
"https://en.wikipedia.org/wiki/Barracuda_(cocktail)",
"https://en.wikipedia.org/wiki/Bee%27s_knees",
"https://en.wikipedia.org/wiki/Bramble_(cocktail)",
"https://en.wikipedia.org/wiki/Canchanchara",
"https://en.wikipedia.org/wiki/Dark_%27n%27_stormy",
"https://en.wikipedia.org/wiki/Espresso_martini",
"https://en.wikipedia.org/wiki/Fernet_con_coca",
"https://en.wikipedia.org/wiki/French_martini",
"https://en.wikipedia.org/wiki/Illegal_(cocktail)",
"https://en.wikipedia.org/wiki/Lemon_drop_(cocktail)",
"https://en.wikipedia.org/wiki/Naked_and_famous_(cocktail)",
"https://en.wikipedia.org/wiki/New_York_sour",
"https://en.wikipedia.org/wiki/Old_Cuban",
"https://en.wikipedia.org/wiki/Paloma_(cocktail)",
"https://en.wikipedia.org/wiki/Paper_plane_(cocktail)",
"https://en.wikipedia.org/wiki/Penicillin_(cocktail)",
"https://en.wikipedia.org/wiki/Russian_spring_punch",
"https://en.wikipedia.org/wiki/Spicy_Fifty",
"https://en.wikipedia.org/wiki/Spritz_(cocktail)",
"https://en.wikipedia.org/wiki/Suffering_bastard",
"https://en.wikipedia.org/wiki/Tipperary_(cocktail)",
"https://en.wikipedia.org/wiki/Tommy%27s_margarita",
"https://en.wikipedia.org/wiki/Trinidad_sour",
"https://en.wikipedia.org/wiki/Ve.n.to",
"https://en.wikipedia.org/wiki/Yellow_bird_(cocktail)"
]

data = []
for url in url_list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find("table", {"class": "infobox"})
    if table:
        caption = table.find("caption")
        tbody = table.find("tbody")
        if tbody:
            trs = tbody.find_all("tr")
            if trs:
                row = {
                    'Name of cocktail': caption.text if caption else '',
                    'Infobox description': trs[0].text if len(trs) > 0 else '',
                    'Picture': trs[1].find("img").get('src', '') if len(trs) > 1 and trs[1].find("img") else '',
                    'Base Spirit': '; '.join([td.text for td in trs[3].find_all("td")]) if len(trs) > 3 else '',
                    'Served': trs[4].find("td").text if len(trs) > 4 and trs[4].find("td") else '',
                    'Garnish': trs[5].find("td").text if len(trs) > 5 and trs[5].find("td") else '',
                    'Drinkware': trs[6].find("td").text if len(trs) > 6 and trs[6].find("td") else '',
                    'Ingredients': '; '.join([td.text for td in trs[7].find_all("td")]) if len(trs) > 7 else '',
                    'Preparation': '; '.join([td.text for td in trs[8].find_all("td")]) if len(trs) > 8 else '',
                    'Commonly Served': trs[9].find("td").text if len(trs) > 9 and trs[9].find("td") else ''
                }
                data.append(row)

df = pd.DataFrame(data)

# Write DataFrame to CSV file
df.to_csv('detail.csv', index=False)