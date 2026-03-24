import cloudscraper
from bs4 import BeautifulSoup
import csv

def main():
    scraper = cloudscraper.create_scraper()

    url = "https://harrypotter.fandom.com/wiki/Category:Characters"

    response = scraper.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    characters = soup.find_all("a", class_="category-page__member-link")

    data = []

    for char in characters:
        name = char.text.strip()
        link = char.get("href")
        data.append([name, link])

    with open("harry_potter_characters.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Link"])
        writer.writerows(data)

    print("Scraping complete!")

if __name__ == "__main__":
    main()
