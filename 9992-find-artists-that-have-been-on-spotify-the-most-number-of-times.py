problem link-->> https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.groupby('artist')['id'].count().reset_index().sort_values(by = 'id').rename(columns={'id':'n_occurences'}).sort_values("n_occurences" , ascending = True)
