#problem link-->> https://platform.stratascratch.com/coding/2024-unique-users-per-client-per-month?code_type=2




# Import your libraries
import pandas as pd

# Start writing code
fact_events['month'] = fact_events['time_id'].dt.month
fact_events.groupby(['client_id' , 'month'])['user_id'].nunique().reset_index().rename(columns={'month':'time_id'})
