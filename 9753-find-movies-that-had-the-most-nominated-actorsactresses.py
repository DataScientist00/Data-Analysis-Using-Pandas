#problem link-->> https://platform.stratascratch.com/coding/9753-find-movies-that-had-the-most-nominated-actorsactresses?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
oscar_nominees.groupby(['year' , 'movie'])['id'].count().reset_index().rename(columns = {'id' : 'n_occurences'}).sort_values(by = 'n_occurences', ascending = False)[['movie' , 'n_occurences']]
