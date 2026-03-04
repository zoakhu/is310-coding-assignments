
favorite_movies = [
  ("10 Things I Hate About You", 1999),
  ("Harry Potter and the Sorcerer's Stone", 2001),
  ("The Princess and the Frog", 2009),
  ("The Dark Knight", 2008)
]

def check_movie(movie):
  name = movie[0]
  year = movie[1]

  if year < 2000:
    print(name + ": This movie was released before 2000")
    return None
  else:
    print(name + ": This movie was released after 2000")
    return name

recent_movies = []

for movie in favorite_movies:
  result = check_movie(movie)

  if result is not None:
    recent_movies.append(result)

print("Movies released after 2000:")
print(recent_movies)
