# Udacity Movie Trailer Website

A part of the Full Stack Web Developer Nanodegree Program.

This project creates a local movie trailer website with movies
of the user's choosing. 

### Prerequisites

```
Python 3.6
webbrowser module
```


## Defining a movie

In entertainment_center.py, use the imported Media module
to define an object of class movie.

The class Movie takes the following arguments:
* Title
* Description
* Poster image URL
* Youtube trailer URL
* IMBD rating

```
black_panther = media.Movie(
    "Black Panther",
    "T'Challa, the King of Wakanda, fights domestic and foreign threats",
    "https://goo.gl/Emnm7Q",
    "https://www.youtube.com/watch?v=xjDjIWPwcPU",
    "7.9")
```

## Launching the trailer website

In entertainment_center.py, use the fresh_tomatoes.open_movies_page
function given a list of movie objects as the argument.

```
movies = [black_panther]
fresh_tomatoes.open_movies_page(movies)
```

## Built With
* Udacity's fresh_tomatoes.py module


## Authors

* **Lasse Alsbirk** 

