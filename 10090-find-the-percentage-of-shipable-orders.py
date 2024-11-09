#problem link-->> https://platform.stratascratch.com/coding/10090-find-the-percentage-of-shipable-orders?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(orders, customers, left_on='cust_id', right_on='id', how='left')
df['address'].count() / len(df['address']) * 100
