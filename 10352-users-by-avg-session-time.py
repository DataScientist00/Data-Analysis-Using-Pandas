#problem link-->> https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=2

# Import your libraries
import pandas as pd
import datetime as dt
# Start writing code
facebook_web_log['date'] = facebook_web_log['timestamp'].dt.date
df1 = facebook_web_log[facebook_web_log['action'] == 'page_load']
df2 = facebook_web_log[facebook_web_log['action'] == 'page_exit']
pl = df1.groupby(['user_id','date'])['timestamp'].max().reset_index().rename(columns={'timestamp':'load_time'})
pe = df2.groupby(['user_id','date'])['timestamp'].max().reset_index().rename(columns={'timestamp':'exit_time'})
df = pd.merge(pl , pe , on = ['user_id','date'],how='inner')
df['second_diff'] = (df['exit_time']-df['load_time']).dt.seconds
df.groupby('user_id')['second_diff'].mean().reset_index().rename(columns={'second_diff':'duration'})
