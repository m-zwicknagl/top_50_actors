import pandas as pd
import tmdb_connect as tmdb

class Data:

    def __init__(self):
        self.df = None

    def import_list(self, str_path_list):

        # Reading a CSV file into a DataFrame
        self.df = pd.read_csv('top_50_actors.csv')

        

    def update_data(self):
        self.df = self.df.drop(["Position","Const","Created","Modified","Description"],axis=1)
        self.df["Movies"] = ""
        self.df["Genres"] = ""
        self.df["Avg Rating"] = ""
        for index, row in self.df.iterrows():
            print(row["Name"])

            actor_details = tmdb.get_actor_movies_with_details(tmdb.get_actor(row["Name"])['id'])
            
            self.df.at[index, "Genres"] = self.__list_to_string(actor_details[2])
            self.df.at[index, "Movies"] = self.__movie_list_to_string(actor_details[0][:5])
            self.df.at[index, "Rating"] = self.__get_avg_rating(movies= actor_details[0])



    def __list_to_string(self,list_input):
        str_out = ""
        for l_item in list_input:
            str_out = str_out + ", " + l_item
        return str_out
    
    def __movie_list_to_string(self, movies_in):
        str_out = ""
        for movie in movies_in:
            str_out = str_out + ", " + movie['title']
        return str_out
    
    def __get_avg_rating(self,movies):
        avg_rating = 0
        for movie in movies:
            avg_rating = avg_rating + movie["rating"]
        avg_rating = avg_rating / len(movies)
            
        

