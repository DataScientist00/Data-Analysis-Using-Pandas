#problem link-->> https://platform.stratascratch.com/coding/9687-find-details-of-oscar-winners-between-2001-and-2009?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
oscar_nominees[(oscar_nominees['year'].between(2001,2009)) & (oscar_nominees['winner']==True)]
