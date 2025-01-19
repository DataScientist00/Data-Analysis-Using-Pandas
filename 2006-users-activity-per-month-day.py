#problem link-->> https://platform.stratascratch.com/coding/2006-users-activity-per-month-day?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
facebook_posts['post_date'] = facebook_posts['post_date'].dt.day
facebook_posts.groupby('post_date').agg(user_activity = ( 'post_id' , 'nunique')).reset_index()
