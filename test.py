from imdb import IMDb

# Create an IMDb object
ia = IMDb()

# Search for the actor by name
actor_name = 'Robert Downey Jr.'  # Replace with the name of your desired actor
actor = ia.search_person(actor_name)  # Get the first result (most likely the correct one)

# Get the actor's filmography
filmography = ia.get_person_filmography(actor)

# Sort the movies by year (or any other criteria you prefer)
movies = filmography.get('actor', [])  # or 'actress' for female actors

# Sort movies by year, in descending order (to get the most recent first)
sorted_movies = sorted(movies, key=lambda x: x['year'], reverse=True)

# Print the titles of the most popular movies (first 10)
print(f"Most popular films of {actor_name}:")
for movie in sorted_movies[:10]:
    title = movie['title']
    year = movie['year']
    print(f"{title} ({year})")
