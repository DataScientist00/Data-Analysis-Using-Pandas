#problem link-->> https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df= sf_restaurant_health_violations[sf_restaurant_health_violations['business_name']=='Roxanne Cafe']
df['year']= df['inspection_date'].dt.year
df.groupby('year')['violation_id'].count().reset_index().sort_index()
