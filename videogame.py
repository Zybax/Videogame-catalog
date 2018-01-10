import webbrowser


class Videogame():
    """ Videogame class describes the attributes of a videogame

        Args:
            name (str): Game's name
            genre (str): Game's genre
            rating (str): Game's rating according to the ESRB
            image (str): The route for the game's cover image
            trailer (str): The url for the game's trailer

        Attributes:
            name (str): Game's name
            genre (str): Game's genre
            rating (str): Game's rating according to the ESRB
            image (str): The route for the game's cover image
            trailer (str): The url for the game's trailer
    """
    def __init__(self, name, genre, rating, image, trailer):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.image = image
        self.trailer = trailer
