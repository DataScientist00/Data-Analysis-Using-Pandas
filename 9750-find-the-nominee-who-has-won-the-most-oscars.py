#problem link-->> https://platform.stratascratch.com/coding/9750-find-the-nominee-who-has-won-the-most-oscars?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df=oscar_nominees[oscar_nominees['winner']==True]
df2 = df.groupby('nominee').agg(n_times_won=('id','count')).reset_index()
df2.nlargest(1,'n_times_won',keep='all')
