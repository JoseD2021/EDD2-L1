from typing import Any, Optional, Tuple
from Node import Node
import pandas as pd

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
        df = pd.read_csv("dataset_movies.csv")
        movie_row = df[df['Title'] == title]

        if not movie_row.empty:
            movie_data = movie_row.iloc[0]
            self.title = movie_data['Title'],
            self.worldwide_earnings = movie_data['Worldwide Earnings'],
            self.domestic_earnings = movie_data['Domestic Earnings'],
            self.domestic_percent = movie_data['Domestic Percent Earnings'],
            self.foreign_earnings = movie_data['Foreign Earnings'],
            self.foreign_percent = movie_data['Foreign Percent Earnings'],
            self.year = movie_data['Year']
        
        else: 
            return None

    def __repr__(self):  #Esta es la forma en la que muestro el nodo
        return f"Película: ({self.title}, {self.year}, Worldwide Earnings: {self.worldwide_earnings})"

#
#def create_movie(title: str) -> Optional[Pelicula]:
#
##Aquí filtro los datos para que escoja la fila por el título
#    movie_row = df[df['Title'] == title]
#    
#    if not movie_row.empty:
#
#        movie_data = movie_row.iloc[0]
#
#        return Pelicula(
#            title=movie_data['Title'],
#            worldwide_earnings=movie_data['Worldwide Earnings'],
#            domestic_earnings=movie_data['Domestic Earnings'],
#            domestic_percent=movie_data['Domestic Percent Earnings'],
#            foreign_earnings=movie_data['Foreign Earnings'],
#            foreign_percent=movie_data['Foreign Percent Earnings'],
#            year=movie_data['Year']
#        )
#    else:
#        print(f"La película '{title}' no fue encontrada.")
#        return None
#
#
#def create_node(title: str) -> Optional[Node]:
#    # Llamo a la función create_movie para obtener el objeto Pelicula
#    movie = create_movie(title)
#    if movie:
#        # Si la encuentra, creo el nodo
#        return Node(movie)
#    return None