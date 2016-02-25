import media
import fresh_tomatoes

#Create movie instances
PULP_FICTION = media.Movie("Pulp Fiction",
                           "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")

GOD_FATHER = media.Movie("The Godfather",
                         "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=YBrs0wvkPls")

HOT_FUZZ = media.Movie("Hot Fuzz",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/HotFuzzUKposter.jpg/250px-HotFuzzUKposter.jpg",
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4")
PI = media.Movie("Pi",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Piposter.jpg/220px-Piposter.jpg",
                 "https://www.youtube.com/watch?v=jo18VIoR2xU")

GRAND_BUDAPEST_HOTEL = media.Movie("Grand Budapest Hotel",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/The_Grand_Budapest_Hotel_Poster.jpg/220px-The_Grand_Budapest_Hotel_Poster.jpg",
                                   "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

#put moives in an array
movies = [PULP_FICTION, GOD_FATHER, HOT_FUZZ, PI, GRAND_BUDAPEST_HOTEL]

#import movies array to html page
fresh_tomatoes.open_movies_page(movies)
