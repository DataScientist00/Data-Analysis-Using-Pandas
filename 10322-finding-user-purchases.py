#problem link-->> https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = amazon_transactions.sort_values(['user_id','created_at'])
df['next_purchase'] = df.groupby('user_id')['created_at'].diff()

df[df['next_purchase'] <= pd.Timedelta(days=7)]['user_id'].unique()
