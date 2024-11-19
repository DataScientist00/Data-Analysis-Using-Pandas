#problem link--> https://platform.stratascratch.com/coding/2029-the-most-popular-client_id-among-users-using-video-and-voice-calls?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = fact_events[fact_events['event_type'].isin(['video call received', 'video call sent', 'voice call received', 'voice call sent'])].groupby('user_id')['event_type'].count().reset_index()
total = fact_events.groupby('user_id')['event_type'].count().reset_index()
df2 = pd.merge(df, total , on='user_id')
df2['percent'] =  df2['event_type_x'] / df2['event_type_y']
df3 = pd.merge(fact_events , df2 , on='user_id')
df3 = df3[df3['percent']>=0.5]
df3 = df3['client_id'].value_counts().reset_index().rename(columns={'index':'client_id','client_id':'a'})
df3[df3['a'] == df3['a'].max()]['client_id']

