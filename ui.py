import tkinter as tk
from tkinter import ttk



class ui:

    root = None

    def __init__(self):
        
        self.root = tk.Tk() 
        # Sample list of top 50 actors (you can replace this with your actual list of actors)
        top_actors = [
            "Tom Hanks", "Meryl Streep", "Leonardo DiCaprio", "Brad Pitt", "Scarlett Johansson",
            "Robert Downey Jr.", "Will Smith", "Johnny Depp", "Angelina Jolie", "Denzel Washington",
            "Nicole Kidman", "Matt Damon", "Tom Cruise", "Sandra Bullock", "Morgan Freeman",
            "Cate Blanchett", "Hugh Jackman", "Jennifer Lawrence", "Julia Roberts", "Chris Hemsworth",
            "Christian Bale", "Kate Winslet", "Samuel L. Jackson", "Al Pacino", "Emma Stone",
            "Matthew McConaughey", "Charlize Theron", "Reese Witherspoon", "Eddie Murphy", "Julia Roberts",
            "Mark Wahlberg", "Harrison Ford", "Keanu Reeves", "Anne Hathaway", "Daniel Day-Lewis",
            "Jodie Foster", "Ryan Gosling", "Harrison Ford", "Robert De Niro", "Helen Mirren",
            "Bradley Cooper", "Amy Adams", "Shailene Woodley", "Joaquin Phoenix", "Hugh Grant",
            "Nicole Kidman", "Daniel Craig", "Ian McKellen", "Hugh Grant", "Vince Vaughn"
        ]

        # Create the main window
        self.root.title("Top 50 Actors")

        # Create a Treeview widget to display the table
        treeview = ttk.Treeview(self.root, columns=("Rank", "Actor"), show="headings")

        # Define the column headings
        treeview.heading("Rank", text="Rank")
        treeview.heading("Actor", text="Actor Name")

        # Add actors to the table (we also include a rank column)
        for idx, actor in enumerate(top_actors, start=1):
            treeview.insert("", "end", values=(idx, actor))

        # Place the Treeview widget in the window
        treeview.pack(expand=True, fill="both")
        self.root.mainloop()

ui = ui()

