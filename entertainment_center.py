# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:08:08 2018

@author: base
"""

import fresh_tomatoes
import Media as media

# Defines an object for each movie with the appropriate variables
am_beauty = media.Movie(
    "American Beauty",
    "Fed up with his boring, stagnant existence, Lester quits his job and \
    decides to reinvent himself",
    "https://goo.gl/2b2DDR",
    "https://www.youtube.com/watch?v=3ycmmJ6rxA8",
    "8.4")

avatar = media.Movie(
    "Avatar",
    "A Marine visits an alien planet",
    "https://goo.gl/EaEdAh",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "7.8")

seven = media.Movie(
    "SE7EN", 
    "Two detectives discover a number of elaborate and grizzly murders",
    "https://goo.gl/42ej4N",
    "https://www.youtube.com/watch?v=znmZoVkCjpI",
    "8.6")

wolf_of_wall_street = media.Movie(
    "The Wolf of Wall Street",
    "The true story of a New York stock broker",
    "https://goo.gl/U2kPNu",
    "https://www.youtube.com/watch?v=pabEtIERlic",
    "8.2")

inception = media.Movie(
    "Inception", 
    "Dom Cobb (Leonardo DiCaprio) is a skilled thief, the best in the \
    dangerous art of extraction: stealing valuable secrets from deep",
    "https://goo.gl/7PE6JX",
    "https://www.youtube.com/watch?v=YoHD9XEInc0",
    "8.8")

justice_league = media.Movie(
    "Justice League",
    "DC's heroes save the world",
    "https://goo.gl/daf31H",
    "https://www.youtube.com/watch?v=r9-DM9uBtVI",
    "6.9")


black_panther = media.Movie(
    "Black Panther",
    "T'Challa, the King of Wakanda, fights domestic and foreign threats",
    "https://goo.gl/Emnm7Q",
    "https://www.youtube.com/watch?v=xjDjIWPwcPU",
    "7.9")


blade_runner = media.Movie(
    "Blade Runner 2049",
    "A blade runner must pursue and try to terminate four replicants who \
    stole a ship in space and have returned to Earth to find their creator",
    "https://goo.gl/YZVLxe",
    "https://www.youtube.com/watch?v=gCcx85zbxz4",
    "8.2")

baby_driver = media.Movie(
    "Baby Driver",
    "After being coerced into working for a crime boss, a young getaway \
    driver finds himself taking part in a heist doomed to fail",
    "https://goo.gl/7wRRj1",
    "https://www.youtube.com/watch?v=z2z857RSfhk",
    "7.7")

# Define list with the movie objects
movies = [am_beauty, 
          avatar, 
          baby_driver, 
          black_panther, 
          blade_runner, 
          inception, 
          justice_league, 
          seven, 
          wolf_of_wall_street]

# Initialise and open a local website with the movie objects. 
# See fresh_tomatoes.py for styling changes to css and HTML
fresh_tomatoes.open_movies_page(movies)
