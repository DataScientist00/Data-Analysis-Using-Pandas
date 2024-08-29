#problem link-->> https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(facebook_employees ,facebook_hack_survey , left_on = 'id' , right_on='employee_id')
df.groupby('location')['popularity'].mean().reset_index()
