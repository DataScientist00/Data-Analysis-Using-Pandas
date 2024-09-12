#problem link-->> https://platform.stratascratch.com/coding/9650-find-the-top-10-ranked-songs-in-2010?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df= billboard_top_100_year_end[billboard_top_100_year_end['year']==2010]
df[df['year_rank'] < 11].drop_duplicates('song_name')[['year_rank','group_name','song_name']].sort_values('year_rank')
