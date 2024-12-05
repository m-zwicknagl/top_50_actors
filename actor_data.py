import pandas as pd

class Data:

    def __init__(self):
        self.df = None

    def import_list(self, str_path_list):

        # Reading a CSV file into a DataFrame
        self.df = pd.read_csv('top_50_actors.csv')

        # Display the first few rows of the DataFrame to check the contents
        print(self.df.head())