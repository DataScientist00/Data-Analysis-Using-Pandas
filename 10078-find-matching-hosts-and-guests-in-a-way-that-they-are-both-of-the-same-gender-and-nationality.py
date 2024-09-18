#problem link-->> https://platform.stratascratch.com/coding/10078-find-matching-hosts-and-guests-in-a-way-that-they-are-both-of-the-same-gender-and-nationality?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(airbnb_hosts ,  airbnb_guests , on = ['nationality' , 'gender'])
df[['host_id','guest_id']].drop_duplicates()
