#problem link-->> https://platform.stratascratch.com/coding/2159-april-may-sign-ups?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
transactions[transactions['transaction_start_date'].dt.month.isin([4,5])]['signup_id'].unique()
