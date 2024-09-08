problem link-->> https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=2


# Import your libraries
import pandas as pd

# Start writing code

dc_bikeshare_q1_2012.groupby('bike_number', as_index = False)['end_time'].max().rename(columns={'end_time':'last_used'}).sort_values(by='last_used' , ascending= False)

