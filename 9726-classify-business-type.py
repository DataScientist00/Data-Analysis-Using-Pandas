#problem link-->>> https://platform.stratascratch.com/coding/9726-classify-business-type/solutions?code_type=2

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code

def category(s):
    nm='other'
    s=s.lower()
    if 'restaurant' in s:
        nm='restaurant'
    elif 'cafe' in s:
        nm='cafe'
    elif 'coffee' in s:
        nm='cafe'
    elif 'café' in s:
        nm='cafe'
    elif 'school' in s:
        nm='school'
        
    return nm
  
df=sf_restaurant_health_violations.copy()
df['business_type']=df['business_name'].apply(category)
df[['business_name','business_type']].drop_duplicates()

