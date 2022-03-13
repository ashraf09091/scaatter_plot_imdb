import imdb


def get_top_movies():
    # creating instance of IMDb
    ia = imdb.IMDb()

    # getting top 250 movies
    search = ia.get_top250_movies()

    data = {}
    for items in search:
        data[items['title']] = {items['rating']: items['votes']}

    return data
