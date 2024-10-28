#problem link-->> https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
sf_transactions['created_at'] = sf_transactions['created_at'].dt.strftime('%Y-%m')
df =  sf_transactions.groupby('created_at')['value'].sum().reset_index().rename(columns={'created_at':'year_month'})
df['prev_value'] = df['value'].shift(1)
df['revenue_diff_pct'] = (100.0 * (df['value'] - df['prev_value']) / df['prev_value']).round(2)
df[['year_month','revenue_diff_pct']]
