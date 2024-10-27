#problem link-->> https://platform.stratascratch.com/coding/10284-popularity-percentage?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
fb = facebook_friends[['user2','user1']]
fb = fb.rename(columns={'user2':'user1' , 'user1':'user2'})
fb = pd.concat([facebook_friends , fb])
df = fb.groupby('user1')['user2'].count().reset_index().rename(columns={'user2':'no_of_friends'})
df['popularity_percent'] = 100.0 * df['no_of_friends'] / df['user1'].count()
df[['user1' , 'popularity_percent']]
