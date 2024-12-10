#problem link-->> https://platform.stratascratch.com/coding/2061-users-with-many-searches?code_type=2


# Import your libraries
import pandas as pd
import datetime as dt

# Start writing code
fb_searches[fb_searches['date'].dt.strftime('%Y-%m') == '2021-08'].groupby('user_id').agg(num_searches = ('search_id','nunique')).reset_index().query('num_searches > 5')['user_id'].count()
