import tkinter as tk
from tkinter import ttk
import actor_data as ad
from actor_data import *

class ui:

    def __init__(self):
        self.root = None
        
        self.root = tk.Tk() 

        self.root.title("Top 50 Actors")

        # Create a Treeview widget to display the table
        treeview = ttk.Treeview(self.root)

        # Define the column headings
        data = ad.Data()
        data.import_list("top_50_actors.csv")
        data.update_data()
        self.df_actor= data.df
        treeview["columns"] = list(self.df_actor.columns)
        for col in self.df_actor.columns:
            treeview.heading(col, text = col)

        # Insert rows into the Treeview widget
        for index, row in self.df_actor.iterrows():
            treeview.insert('', 'end', values=list(row))
        
        # Place the Treeview widget in the window
        treeview.pack(expand=True, fill="both")
        self.root.mainloop()

if __name__ == "__main__":
    ui = ui()



