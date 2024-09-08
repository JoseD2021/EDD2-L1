from typing import Any, Optional, Tuple
from Node import Node
import pandas as pd
df = pd.read_csv("dataset_movies.csv")

class Movie:
    def __init__(self, title: Optional[str] = None, worldwide_earnings: Optional[int] = None, domestic_earnings: Optional[int] = None,
        domestic_percent: Optional[float] = None, foreign_earnings: Optional[int] = None, foreign_percent: Optional[float] = None, year: Optional[int] = None) -> None:
        self.title = title
        self.worldwide_earnings = worldwide_earnings
        self.domestic_earnings = domestic_earnings
        self.domestic_percent = domestic_percent
        self.foreign_earnings = foreign_earnings
        self.foreign_percent = foreign_percent
        self.year = year

    def createMovie (self,title:str):
        movie_row = df[df['Title'] == title]
        if not movie_row.empty:
            movie_data = movie_row.iloc[0]
            self.title = movie_data['Title']
            self.worldwide_earnings = movie_data['Worldwide Earnings']
            self.domestic_earnings = movie_data['Domestic Earnings']
            self.domestic_percent = movie_data['Domestic Percent Earnings']
            self.foreign_earnings = movie_data['Foreign Earnings']
            self.foreign_percent = movie_data['Foreign Percent Earnings']
            self.year = int(movie_data['Year'])
            return self
        
        else: 
            return None

    def __repr__(self):  #Esta es la forma en la que muestro el nodo
        return f"Película: ({self.title}, {self.year}, Worldwide Earnings: {self.worldwide_earnings})"

@staticmethod
def create_node(title: str) -> Optional[Node]:
    movie_instance = Movie()  # Crea una instancia de Movie
    movie = movie_instance.createMovie(title)  # Llama al método de instancia
    if movie:
        return Node(movie)
    return None