#problem link-->> https://platform.stratascratch.com/coding/9932-women-in-the-olympics-before-world-war-2?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
olympics_athletes_events.query("sex == 'F' & year < 1939")[['name']].drop_duplicates()
