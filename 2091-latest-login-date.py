#problem link-->> https://platform.stratascratch.com/coding/2091-latest-login-date?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
players_logins.groupby('player_id').agg(login_date = ('login_date','max')).reset_index()
