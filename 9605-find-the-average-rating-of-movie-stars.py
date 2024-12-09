
#problem link-->> https://platform.stratascratch.com/coding/9605-find-the-average-rating-of-movie-stars?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = nominee_filmography.groupby('name')['rating'].mean().reset_index()
df1 = pd.merge(nominee_information , df , on = 'name' , how='left')[['birthday','name','rating']].sort_values(by='birthday',ascending=True)
df1['birthday'] = df1['birthday'].dt.strftime('%Y-%m-%d')
