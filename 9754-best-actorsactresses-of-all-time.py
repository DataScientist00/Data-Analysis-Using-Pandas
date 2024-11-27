#problem link-->> https://platform.stratascratch.com/coding/9754-best-actorsactresses-of-all-time?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = oscar_nominees[oscar_nominees['winner'] == True]
df.groupby('nominee').agg(n_occurences=('id','count')).reset_index().sort_values(by='n_occurences' , ascending= False)
