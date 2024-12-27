#problem link-->> https://platform.stratascratch.com/coding/9751-nominees-without-an-oscar?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
winners = oscar_nominees[oscar_nominees['winner'] == True]['nominee']

oscar_nominees[~ oscar_nominees['nominee'].isin(list(winners))].groupby('nominee').agg(n_times_nominated=('id','count')).reset_index().sort_values(by='n_times_nominated' , ascending = False)
