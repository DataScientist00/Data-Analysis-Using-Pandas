#problem link-->> https://platform.stratascratch.com/coding/2107-primary-key-violation?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
dim_customer.groupby('cust_id').agg(n_occurences=('cust_id','count')).reset_index().query('n_occurences > 1')
