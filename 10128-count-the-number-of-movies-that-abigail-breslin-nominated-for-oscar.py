#problem link-->> https://platform.stratascratch.com/coding/10128-count-the-number-of-movies-that-abigail-breslin-nominated-for-oscar?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = oscar_nominees[oscar_nominees['nominee'] == 'Abigail Breslin']
df.groupby('nominee')['year'].count()
