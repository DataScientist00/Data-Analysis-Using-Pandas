#problem link-->> https://platform.stratascratch.com/coding/10171-find-the-genre-of-the-person-with-the-most-number-of-oscar-winnings?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = oscar_nominees.merge(nominee_information , left_on = 'nominee' ,right_on ='name' , how ='inner' ).query('winner == True').groupby(['nominee' , 'top_genre']).size().to_frame('num').reset_index()

df['rank'] = df['num'].rank(method='dense' , ascending =False)
df.query('rank == 1').sort_values(by = 'nominee')[['top_genre']].head(1)
