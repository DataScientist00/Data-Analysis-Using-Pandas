#problem link-->> https://platform.stratascratch.com/coding/2133-first-three-most-watched-videos?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
videos_watched['ab'] = videos_watched.groupby('user_id')['watched_at'].rank(method='dense',ascending = True)
first3 = videos_watched[videos_watched['ab'] <= 3]
df = first3.groupby('video_id').agg(n_in_first_3 = ('video_id','count')).reset_index()
df['rank'] = df['n_in_first_3'].rank(method='dense',ascending=False)
df[df['rank'] <=3][['video_id','n_in_first_3']]
