#problem link-->> https://platform.stratascratch.com/coding/2102-flags-per-video?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df= user_flags
df['num_unique_users'] = df['user_firstname'].fillna('FNU')+' '+df['user_lastname'].fillna('LNU')
df=df[df['flag_id'].isnull()==False]
df = df.groupby('video_id')['num_unique_users'].nunique().reset_index()
