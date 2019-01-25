# ud036_StarterCode
Source code for a Movie Trailer website.

This program contains 3 main python files:
  - media.py
  - entertainment_center.py
  - fresh_tomatoes.py

The credits of this codes are from udacity and IMDbPY code examples.

The media.py file contains a class named Movie that defines the structure for a movies.

The entertainment_center.py is the file where the objects of the class movie are created
and initiates the fresh_tomatoes method to create the .html page.

The module IMDbPY is used in this program as an API to get movies data. (source: https://imdbpy.sourceforge.io/)

  Example of how to choose a list of movies:
      mybestmovies = {
                '%mission: impossible - fallout%':'https://www.youtube.com/watch?v=XiHiW4N7-bo',
                'The Angel':'https://www.youtube.com/watch?v=z0q2WbXQWbw',
                'Avengers: Infinity War':'https://www.youtube.com/watch?v=hA6hldpSTF8',
                '007 Spectre':'https://www.youtube.com/watch?v=z4UDNzXD3qA',
                'The Resistence Banker':'https://www.youtube.com/watch?v=31pzuZSvzvU',
                'The Revenant':'https://www.youtube.com/watch?v=LoebZZ8K5N0'
                }
This list of movies is used as input for the search of movie´s data using IMDb API. This API can´t get movie trailer url, so we need to insert it.

On fresh_tomatoes.py file are defined the html, css and javascript to create the mains page.
Two main methods are  create_movie_tiles_content and open_movies_page.

The css and html model was modified to include the movie storyline.

