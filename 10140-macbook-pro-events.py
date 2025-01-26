#problem link -- >> https://platform.stratascratch.com/coding/10140-macbook-pro-events?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(playbook_events , playbook_users , on = 'user_id')

df1 = df[(df['device'] == 'macbook pro') & (df['location'] == 'Argentina') & (df['language'] != 'Spanish')]
df1.groupby(['company_id' , 'language']).agg(n_events = ('event_name','count')).reset_index()
