#problem link-->> https://platform.stratascratch.com/coding/2072-active-users-per-platform?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
user_sessions.groupby('platform')['user_id'].nunique().reset_index()
