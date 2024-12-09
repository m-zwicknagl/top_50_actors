import tmdbsimple as tmdb

# Set up your API key from TMDb
tmdb.API_KEY = 'x'  # Replace with your actual TMDb API key

def search_actor(actor_name):
    """
    Search for an actor by name and return their details.
    """
    search = tmdb.Search()
    response = search.person(query=actor_name)
    if not search.results:
        return None
    # Return the first result's details
    return search.results[0]

def get_actor_movies_with_details(actor_id):
    """
    Get all movies for a given actor with release year, popularity, and genres.
    """
    person = tmdb.People(actor_id)
    response = person.movie_credits()
    cast_movies = response.get('cast', [])
    list_genres = []

    # Add popularity, release year, and genres for each movie
    for movie in cast_movies:
        movie_details = tmdb.Movies(movie['id']).info()
        movie['popularity'] = movie_details.get('popularity', 0)  # Default to 0 if missing
        movie['rating'] = movie_details.get('vote_average', 0)  # Default to 0 for missing ratings
        movie['release_year'] = (
            movie.get('release_date', '').split('-')[0] if movie.get('release_date') else 'Unknown'
        )
        for genre in movie_details.get('genres', []):
            movie['genres'] = genre['name'] 
            
            if genre["name"] not in list_genres :
                list_genres.append(genre["name"])

    # Sort movies by popularity (highest first)
    cast_movies.sort(key=lambda m: m['popularity'], reverse=True)

    return cast_movies,  list_genres

def get_actor(str_actor_name):
    actor = search_actor(str_actor_name)
    return actor


