#problem link--->> https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.sort_values(by='profits' , ascending = False)[['company','profits']].head(3)
