#problem link-->> https://platform.stratascratch.com/coding/2067-low-fat-and-recyclable?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = facebook_products[(facebook_products['is_low_fat'] == 'Y') & (facebook_products['is_recyclable'] == 'Y')]
len(df)/len(facebook_products) * 100.0
