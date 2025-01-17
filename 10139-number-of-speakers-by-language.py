#problem link-->> https://platform.stratascratch.com/coding/10139-number-of-speakers-by-language?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = playbook_events.merge(playbook_users , how = 'left' , on = 'user_id')[['location' , 'language' , 'user_id']]
df.groupby(['location' , 'language']).agg(n_speakers = ('user_id' , 'nunique')).reset_index().sort_values(by = 'location')
