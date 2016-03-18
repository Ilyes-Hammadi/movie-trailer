import json

from models import Movie
"""
python module to generate data from a json file
"""
def get_movies():
    # Open and reas the json file
    data = open('../movies.json').read()
    # Parse the data into a python dictanory
    movies_list = json.loads(data)

    movies = []

    # Transfer the data from the array into an array of Movies objects
    for movie in movies_list:
        # Create an object with the apropriate data and append it to the list
        movies.append(
            Movie(movie['title'], movie['story_line'], movie['poster_image_url'], movie['trailer_youtube_url'],
                  movie['release_date']))

    return movies
