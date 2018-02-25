# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:32:45 2018

@author: base
"""

import webbrowser


class Movie():
    """ 
    Movie objects contain information and a show_trailer method for a movie.
    """
    # Initialize the Movie class. I have added IMDB rating as an attribute
    def __init__(self, 
                 title, 
                 storyline, 
                 poster_image_url, 
                 trailer_youtube_url, 
                 imdb_rating):

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_rating = imdb_rating

    # Defines method that opens up a web browser
    # and displays the youtube trailer 

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
