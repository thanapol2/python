import pandas as pd
import numpy as np

ratingsList = [i.strip().split(",") for i in open('ratings.csv', 'r').readlines()]
# users_list = [i.strip().split(",") for i in open('users.dat', 'r').readlines()]
moviesList = [i.strip().split(",") for i in open('movies.csv', 'r', encoding="utf8").readlines()]

ratingsDataFrame = pd.DataFrame(ratingsList, columns = ['UserID', 'MovieID', 'Rating', 'Timestamp'], dtype = int)
ratingsDataFrame.drop(ratingsDataFrame.index[:1], inplace=True)
# print(ratings_df.head())

for index, val in enumerate(moviesList):
    if len(val)>3:
        moviesList[index] = [val[0], ','.join(val[1:len(val) - 1]), val[-1]]


moviesDataFrame = pd.DataFrame(moviesList, columns = ['MovieID', 'Title', 'Genres'])

moviesDataFrame.drop(moviesDataFrame.index[:1], inplace=True)
moviesDataFrame['MovieID'] = moviesDataFrame['MovieID'].apply(pd.to_numeric)
print(moviesDataFrame.head())

