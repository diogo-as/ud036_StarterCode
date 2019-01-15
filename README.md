# ud036_StarterCode
Source code for a Movie Trailer website.

This program contains 3 main python files:
  - media.py
  - entertainment_center.py
  - fresh_tomatoes.py

The credits of this codes are from udacity.

The media.py file contains a class named Movie that defines the structure for a movies.

The entertainment_center.py is the file where the objects of the class movie are created
and initiates the fresh_tomatoes method to create the .html page.

  Example of how to create a movie:
  the_angel = media.Movie("The Angel",
                          "The egyptian spy who saved Israel",
                          "https://m.media-amazon.com/images/M/MV5BMTEzOTY5ODA2MDReQTJeQWpwZ15BbWU4MDI5NDkyMTYz._V1_SY1000_CR0,0,682,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=z0q2WbXQWbw")

  Don´t forget to insert the neu movie object on the list:

      movies = [mi_fallout, the_angel, avengers_infinity_war, spectre, resistence_banker, the_revenant]

On fresh_tomatoes.py file are defined the html, css and javascript to create the mains page.
Two main methods are  create_movie_tiles_content and open_movies_page.

The html model was modified to include the movie storyline.

For while, the css and javascript are not modified.
