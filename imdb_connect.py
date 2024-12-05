import imdb



class imdb_connect:

    # Initialize IMDb instance
    
    
    def __init__(self):
        self.ia = imdb.Cinemagoer()

    # Function to get all movies by an actor's name
    def get_movies_by_actor(self,actor_name):
        # Search for the actor by name
        people = self.ia.search_person(actor_name)
        
        if people:
            # Get the first person in the search result (if multiple results, you can refine)
            actor = people[0]
            print(actor)
            actor_id = actor.personID
            
            # Get the actor's filmography
            actor_movies = self.ia.get_person_filmography(actor_id)
            
            if actor_movies:
                print(f"Movies featuring {actor_name}:")
                # Iterate through the movies and print the title and year
                for movie in actor_movies['titlesRefs']:
                    #title = movie.get('title')
                    #year = movie.get('year', 'Unknown Year')
                    print(movie)
            else:
                print(f"No movies found for {actor_name}.")
        else:
            print(f"Actor {actor_name} not found.")


icon = imdb_connect()
icon.get_movies_by_actor("Tom Hanks")
