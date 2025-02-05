#problem link-->> https://platform.stratascratch.com/coding/2025-users-exclusive-per-client?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
fact_events['n_clients'] = fact_events.groupby('user_id')['client_id'].transform('nunique')
fact_events.query("n_clients == 1").groupby('client_id')['user_id'].nunique().reset_index()
