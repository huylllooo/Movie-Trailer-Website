import media
import fresh_tomatoes

BvS = media.Movie("Batman v Superman: Dawn of Justice",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                "https://www.youtube.com/watch?v=0WWzgGyAH6Y")

wonder_woman = media.Movie("Wonder Woman",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUxNjQ5MjAyOF5BMl5BanBnXkFtZTgwMjIzOTA1MDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Tgk_63b-Mrw")

justice_league = media.Movie("Justice League",
                        "https://s-media-cache-ak0.pinimg.com/originals/81/1c/96/811c962100bce08f35cb8901f0bf0677.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=fIHH5-HVS9o")

# List of all movies
moviesList = [BvS, wonder_woman, justice_league]

fresh_tomatoes.open_movies_page(moviesList)
