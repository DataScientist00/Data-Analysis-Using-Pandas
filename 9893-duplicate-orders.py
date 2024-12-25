#problem link-->>https://platform.stratascratch.com/coding/9893-duplicate-orders?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
orders.groupby('cust_id').agg(num=('id','count')).reset_index().query('num > 3')[['cust_id']]
