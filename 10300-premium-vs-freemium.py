#problem link-->> https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(ms_download_facts , ms_user_dimension , on = 'user_id' , how = 'left')
df2 = pd.merge(df , ms_acc_dimension , on='acc_id', how = 'left')

df3 = df2.pivot_table(index='date' , columns = 'paying_customer' , values='downloads' , aggfunc='sum').reset_index()

df3[df3['no'] > df3['yes']]
