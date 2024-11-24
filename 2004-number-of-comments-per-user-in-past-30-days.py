#problem link-->> https://platform.stratascratch.com/coding/2004-number-of-comments-per-user-in-past-30-days?code_type=2


# Import your libraries
import pandas as pd
import datetime as dt

# Start writing code
start_date = pd.to_datetime('2020-02-10') - dt.timedelta(days=30)
end_date = pd.to_datetime('2020-02-10')
df = fb_comments_count[fb_comments_count['created_at'].between(start_date , end_date)]
df.groupby('user_id')['number_of_comments'].sum().reset_index()
