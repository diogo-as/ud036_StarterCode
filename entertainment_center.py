import fresh_tomatoes
import media
from imdb import IMDb


# create an instance of imbd class
ia = IMDb()
# Creating a dictionarie with my best movies title and trailer url
mybestmovies = {
                '%mission: impossible - fallout%': 'https://www.youtube.com/watch?v=XiHiW4N7-bo',
                'The Angel': 'https://www.youtube.com/watch?v=z0q2WbXQWbw',
                'Avengers: Infinity War': ' https://www.youtube.com/watch?v=hA6hldpSTF8',
                '007 Spectre': 'https://www.youtube.com/watch?v=z4UDNzXD3qA',
                'The Resistence Banker': 'https://www.youtube.com/watch?v=31pzuZSvzvU',
                'The Revenant': 'https://www.youtube.com/watch?v=LoebZZ8K5N0'
                }
# Creating a list of movie objects
bestmovieslist = []

for name in mybestmovies.keys():
    movielist = ia.search_movie(name)  # search movie by the string of title
    moviechoice = movielist[0]  # choice the first result
    ia.update(moviechoice)  # update with full data
    storylist = moviechoice.get('plot')  # get list of storylist
    storyline = storylist[0]  # get the first storyline
    cover = moviechoice.get('full-size cover url')  # get the full cover url
    movie_trailer = mybestmovies[name]  # get the movie trailer
    bestmovieslist.append(media.Movie(moviechoice, storyline, cover, movie_trailer))  # create an object movie with the variables needded

# Passing movie list to the method open_movies_page
fresh_tomatoes.open_movies_page(bestmovieslist)
