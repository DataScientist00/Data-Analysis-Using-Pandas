#problem link-->> https://platform.stratascratch.com/coding/2054-consecutive-days?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
sf_events.drop_duplicates(inplace = True)
sf_events['rank'] = sf_events.groupby('user_id')['date'].rank(method = 'dense')
sf_events['diff'] =  sf_events['date'] - pd.to_datetime(sf_events['rank'] , format = '%d')

sf_events.groupby(['user_id' , 'diff']).agg(num=('account_id' , 'count')).reset_index().query('num >=3')[['user_id']]
