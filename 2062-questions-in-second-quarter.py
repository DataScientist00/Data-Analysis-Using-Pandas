#problem link-->> https://platform.stratascratch.com/coding/2062-questions-in-second-quarter?code_type=2

# Import your libraries
import pandas as pd
import datetime as dt

# Start writing code
fb_searches[(fb_searches['date'].dt.year == 2021) & (fb_searches['date'].dt.quarter == 2)]['search_id'].count()
