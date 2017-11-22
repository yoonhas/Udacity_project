import webbrowser


#Class file that generates an instace with name, story, image, trailer, director, and opeing date
class Movie():
    def __init__(self, movie_title, storyline, image, trailer, director, date):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
        self.director = director
        self.open_date = date

    def show_trailer(self):
        webbrowser.open(self.trailer) #open a window for tailer
