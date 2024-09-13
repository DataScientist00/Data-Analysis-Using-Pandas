#problem link-->> https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?tabname=solutions&code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(airbnb_hosts , airbnb_units , on = 'host_id')
df = df[(df['age'] < 30 ) & (df['unit_type'] == 'Apartment')].drop_duplicates()
df.groupby('nationality')['unit_id'].count().reset_index().sort_values(by = 'unit_id' , ascending = False).rename(columns={'unit_id' : 'apartment_count'})
