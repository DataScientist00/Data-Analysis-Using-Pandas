#problem link-->> https://platform.stratascratch.com/coding/9991-top-ranked-songs?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position'] == 1]
df.groupby('trackname')['id'].count().reset_index().sort_values('id' , ascending = False)
