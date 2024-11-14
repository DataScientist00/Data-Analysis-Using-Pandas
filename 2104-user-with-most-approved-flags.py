#problem link-->> https://platform.stratascratch.com/coding/2104-user-with-most-approved-flags?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(user_flags , flag_review , on='flag_id' , how='left')
df1 = df[(df['reviewed_by_yt'] == True) * (df['reviewed_outcome'
    ] == 'APPROVED')]
df1['full_user_name'] = df1['user_firstname'] +' '+df1['user_lastname']
df2 = df1.groupby('full_user_name')['video_id'].nunique().reset_index()
df2[df2['video_id'] == df2['video_id'].max()]['full_user_name']
