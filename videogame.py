import webbrowser


class Videogame():
    def __init__(self, name, genre, rating, image, trailer):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.image = image
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
