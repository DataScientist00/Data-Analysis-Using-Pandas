#problem link-->> https://platform.stratascratch.com/coding/9663-find-the-most-profitable-company-in-the-financial-sector-of-the-entire-world-along-with-its-continent?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = forbes_global_2010_2014[forbes_global_2010_2014['sector']=='Financials']
df[df['profits'] == df['profits'].max()][['company' , 'continent']]
