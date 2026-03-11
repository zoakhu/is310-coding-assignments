from rich.console import Console
from rich.table import Table

console = Console()

console.print("Here is some initial movie data:", style="bold cyan")

table = Table(title="Disney Movies")
table.add_column("Released", style="cyan")
table.add_column("Title", style="magenta")
table.add_column("Box Office")

table.add_row("Dec 11, 2009", "The Princess and the Frog", "$271,000,000")
table.add_row("Nov 22, 2013", "Frozen", "$1,284,000,000")

console.print(table)

console.print("\nNow enter your own movie data:\n", style="bold cyan")

movies = []

while True:
    
    title = input("Enter movie title: ")
    release = input("Enter release date: ")
    box = input("Enter box office: ")

    console.print("\nYou entered:", style="bold yellow")
    console.print(f"Title: {title}")
    console.print(f"Release Date: {release}")
    console.print(f"Box Office: {box}")

    confirm = input("Is this correct? (yes/no): ")

    if confirm == "yes":
        movies.append([release, title, box])
        console.print("Movie saved!", style="green")
    else:
        console.print("Let's try again.", style="red")
        continue

    again = input("Do you want to add another movie? (yes/no): ")

    if again != "yes":
        break


# save data to file
file = open("movies.txt", "w")

for movie in movies:
    file.write(",".join(movie) + "\n")

file.close()

console.print("\nData saved to movies.txt", style="bold green")