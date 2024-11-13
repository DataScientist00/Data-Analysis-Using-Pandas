#problem link-->> https://platform.stratascratch.com/coding/2099-election-results?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = voting_results.dropna()
df1 =df.groupby('voter')['candidate'].count().reset_index().rename(columns={'candidate':'num_of_people_voted'})
df1['total'] = round(1/df1['num_of_people_voted'] , 3)
df2 =  pd.merge(df,df1 , on='voter' , how='left')
df3 = df2.groupby('candidate')['total'].sum().reset_index()
df3['rank'] = df3['total'].rank(method='dense' , ascending=False)
df3[df3['rank']==1]['candidate']
