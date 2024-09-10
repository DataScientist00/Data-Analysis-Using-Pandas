#problem link-->> https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_contacts.groupby('id_guest')['n_messages'].sum().reset_index().sort_values(by = 'n_messages' , ascending = False)

df['ranking'] = df['n_messages'].rank(method = 'dense' , ascending=False)
df[['ranking','n_messages','id_guest']]


