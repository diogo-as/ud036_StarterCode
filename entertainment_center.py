import fresh_tomatoes
import media

mi_fallout = media.Movie("MI - Fallout",
                        "Ethan race against time after a mission gone wrong",
                        "https://upload.wikimedia.org/wikipedia/pt/2/21/Mission_Impossible_%E2%80%93_Fallout.jpg",
                        "https://www.youtube.com/watch?v=XiHiW4N7-bo")

the_angel = media.Movie("The Angel",
                     "The egyptian spy who saved Israel",
                     "https://m.media-amazon.com/images/M/MV5BMTEzOTY5ODA2MDReQTJeQWpwZ15BbWU4MDI5NDkyMTYz._V1_SY1000_CR0,0,682,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=z0q2WbXQWbw")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
                      "The avengers and their allies against Thanos",
                      "https://upload.wikimedia.org/wikipedia/pt/9/90/Avengers_Infinity_War.jpg",
                      "https://www.youtube.com/watch?v=hA6hldpSTF8")

spectre = media.Movie("007 Spectre",
                      "007 against Spectre, a terrorist organization",
                      "https://upload.wikimedia.org/wikipedia/pt/1/1a/Spectre-007.png",
                      "https://www.youtube.com/watch?v=z4UDNzXD3qA")

resistence_banker = media.Movie("The Resistence Banker",
                      "A banker in occupied Amsterdam setting up a clandestine bank to finance resistance",
                      "https://upload.wikimedia.org/wikipedia/en/d/dd/The_Resistance_Banker.jpg",
                      "https://www.youtube.com/watch?v=31pzuZSvzvU")

the_revenant = media.Movie("The Revenant",
                      "A man fights for survival after being mauled by a bear and left to dead",
                      "https://upload.wikimedia.org/wikipedia/pt/0/03/TheRevenant-Poster.png",
                      "https://www.youtube.com/watch?v=LoebZZ8K5N0")

#print (spectre.storyline)
#spectre.show_trailer()
movies = [mi_fallout, the_angel, avengers_infinity_war, spectre, resistence_banker, the_revenant]
fresh_tomatoes.open_movies_page(movies)
