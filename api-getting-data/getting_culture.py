import requests
import json

API_url = https://hp-api.onrender.com/
hp_url = "https://hp-api.onrender.com/api/character/9e3f7ce4-b9a7-4244-b709-dae5c1f1d4a8"

hp_response = requests.get(hp_url)

if hp_response.status_code == 200:
    hp_data = hp_response.json()
    print("HARRY POTTER DATA:")
    print(hp_data)
else:
    print("Error:", hp_response.status_code)

# Get character name
character_name = hp_data[0]["name"]


api_key =

europeana_url = f"https://api.europeana.eu/record/v2/search.json?query={character_name}&wskey={api_key}"

europeana_response = requests.get(europeana_url)

if europeana_response.status_code == 200:
    europeana_data = europeana_response.json()
    print("\nEUROPEANA DATA:")
    print(europeana_data)
else:
    print("Error:", europeana_response.status_code)



if "apikey" in europeana_data:
    del europeana_data["apikey"]

output = {
    "harry_potter_character": hp_data[0],
    "europeana_results": europeana_data["items"] if "items" in europeana_data else []
}

with open("harrypotter_culture_data.json", "w") as file:
    json.dump(output, file, indent=4)

print("\nSaved to harrypotter_culture_data.json")
