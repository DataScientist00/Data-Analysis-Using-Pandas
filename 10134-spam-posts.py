#problem link-->> https://platform.stratascratch.com/coding/10134-spam-posts?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df1 = pd.merge(facebook_posts , facebook_post_views , on = 'post_id' , how = 'inner')
df1['spam'] = df1['post_keywords'].str.contains('spam')
df2 = df1.groupby('post_date').agg({'spam':'sum','viewer_id':'count'}).reset_index()
df2['spam_share'] = df2['spam'] / df2['viewer_id'] * 100
df2[['post_date','spam_share']]
