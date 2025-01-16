#problem link-->> https://platform.stratascratch.com/coding/2141-most-recent-employee-login-details?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
worker_logins.groupby('worker_id')['login_timestamp'].max().reset_index()
