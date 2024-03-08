import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint
from io import StringIO

URLs = [
    "https://en.wikipedia.org/wiki/Alexander_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Americano_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Angel_face_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Aviation_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Between_the_sheets_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Boulevardier_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Brandy_crusta",
"https://en.wikipedia.org/wiki/A/wiki/Casino_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Clover_Club_cocktail",
"https://en.wikipedia.org/wiki/A/wiki/Daiquiri",
"https://en.wikipedia.org/wiki/A/wiki/Martini_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Gin_fizz",
"https://en.wikipedia.org/wiki/A/wiki/Hanky_panky_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/John_Collins_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Last_word_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Manhattan_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Martinez_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Mary_Pickford_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Monkey_gland_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Negroni",
"https://en.wikipedia.org/wiki/A/wiki/Old_fashioned_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Paradise_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Planter%27s_punch",
"https://en.wikipedia.org/wiki/A/wiki/Porto_flip",
"https://en.wikipedia.org/wiki/A/wiki/Ramos_fizz",
"https://en.wikipedia.org/wiki/A/wiki/Rusty_nail_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Sazerac",
"https://en.wikipedia.org/wiki/A/wiki/Sidecar_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Stinger_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Tuxedo_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Vieux_Carr%C3%A9_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Whiskey_sour",
"https://en.wikipedia.org/wiki/A/wiki/White_lady_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Bellini_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Black_Russian",
"https://en.wikipedia.org/wiki/A/wiki/Bloody_Mary_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Caipirinha",
"https://en.wikipedia.org/wiki/A/wiki/Champagne_cocktail",
"https://en.wikipedia.org/wiki/A/wiki/Corpse_reviver#Corpse_reviver_#2_and_#2A",
"https://en.wikipedia.org/wiki/A/wiki/Cosmopolitan_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Rum_and_Coke",
"https://en.wikipedia.org/wiki/A/wiki/French_75_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/French_Connection_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Golden_dream_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Grasshopper_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Hemingway_special",
"https://en.wikipedia.org/wiki/A/wiki/Horse%27s_neck",
"https://en.wikipedia.org/wiki/A/wiki/Irish_coffee",
"https://en.wikipedia.org/wiki/A/wiki/Kir_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Long_Island_iced_tea",
"https://en.wikipedia.org/wiki/A/wiki/Mai_Tai",
"https://en.wikipedia.org/wiki/A/wiki/Margarita",
"https://en.wikipedia.org/wiki/A/wiki/Mimosa_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Mint_julep",
"https://en.wikipedia.org/wiki/A/wiki/Mojito",
"https://en.wikipedia.org/wiki/A/wiki/Moscow_mule",
"https://en.wikipedia.org/wiki/A/wiki/Pi%C3%B1a_colada",
"https://en.wikipedia.org/wiki/A/wiki/Pisco_sour",
"https://en.wikipedia.org/wiki/A/wiki/Sea_breeze_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Sex_on_the_beach",
"https://en.wikipedia.org/wiki/A/wiki/Singapore_sling",
"https://en.wikipedia.org/wiki/A/wiki/Tequila_sunrise",
"https://en.wikipedia.org/wiki/A/wiki/Vesper_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Zombie_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Barracuda_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Bee%27s_knees",
"https://en.wikipedia.org/wiki/A/wiki/Bramble_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Canchanchara",
"https://en.wikipedia.org/wiki/A/wiki/Dark_%27n%27_stormy",
"https://en.wikipedia.org/wiki/A/wiki/Espresso_martini",
"https://en.wikipedia.org/wiki/A/wiki/Fernet_con_coca",
"https://en.wikipedia.org/wiki/A/wiki/French_martini",
"https://en.wikipedia.org/wiki/A/wiki/Illegal_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Lemon_drop_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Naked_and_famous_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/New_York_sour",
"https://en.wikipedia.org/wiki/A/wiki/Old_Cuban",
"https://en.wikipedia.org/wiki/A/wiki/Paloma_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Paper_plane_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Penicillin_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Russian_spring_punch",
"https://en.wikipedia.org/wiki/A/wiki/Spicy_Fifty",
"https://en.wikipedia.org/wiki/A/wiki/Spritz_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Suffering_bastard",
"https://en.wikipedia.org/wiki/A/wiki/Tipperary_(cocktail)",
"https://en.wikipedia.org/wiki/A/wiki/Tommy%27s_margarita",
"https://en.wikipedia.org/wiki/A/wiki/Trinidad_sour",
"https://en.wikipedia.org/wiki/A/wiki/Ve.n.to",
"https://en.wikipedia.org/wiki/A/wiki/Yellow_bird_(cocktail)"
]

# Define df as an empty DataFrame
df = pd.DataFrame()

dfs = []  # List to store DataFrames

for URL in URLs:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html5lib")
    cocktail = soup.find(class_ = "infobox")

if cocktail.name == 'table':
    # Convert the BeautifulSoup object to a string and read it into a DataFrame
    df = pd.read_html(StringIO(str(cocktail)))[0]
else:
    print(f'The object is not a table, it is a {cocktail.name}')

    # Transpose the DataFrame to flatten it into a single row
    df = df.transpose()

    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate the DataFrames in the list into a single DataFrame
df = pd.concat(dfs, ignore_index=True)

# Write the DataFrame to a CSV file
df.to_csv('alextable2.csv', index=False)