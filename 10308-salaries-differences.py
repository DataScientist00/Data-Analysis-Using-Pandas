#problem link-->> https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(db_employee , db_dept , left_on = 'department_id',right_on='id')
abs(df[df['department'].isin(['marketing','engineering'])].groupby('department')['salary'].max().reset_index()['salary'].diff().iloc[1])
