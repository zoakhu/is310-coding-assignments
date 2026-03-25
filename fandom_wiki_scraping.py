import cloudscraper
from bs4 import BeautifulSoup
import csv
import time

scraper = cloudscraper.create_scraper()

characters = [
    "Harry_Potter",
    "Hermione_Granger",
    "Ron_Weasley",
    "Albus_Dumbledore",
    "Severus_Snape",
    "Draco_Malfoy",
    "Sirius_Black",
    "Rubeus_Hagrid",
    "Luna_Lovegood",
    "Neville_Longbottom"
]

def get_infobox_value(soup, field):
    item = soup.find(attrs={"data-source": field})
    if item:
        value = item.find(class_="pi-data-value")
        if value:
            return value.get_text(strip=True)
    return ""

characters_data = []

for name in characters:
    url = "https://harrypotter.fandom.com/wiki/" + name
    print("Scraping:", url)

    response = scraper.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    character_info = {
        "name": name.replace("_", " "),
        "house": get_infobox_value(soup, "house"),
        "gender": get_infobox_value(soup, "gender"),
        "link": url
    }

    characters_data.append(character_info)
    print("Done:", character_info["name"])


with open("harry_potter_characters.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=characters_data[0].keys())
    writer.writeheader()
    writer.writerows(characters_data)

print("Saved CSV!")
print("Scraped", len(characters_data), "characters.")