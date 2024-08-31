#problem link-->> https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(employee , employee , how = 'inner' , left_on='manager_id' , right_on = 'id' , suffixes = ('_x' , '_y'))
df.loc[df['salary_x'] > df['salary_y'] , ['first_name_x' , 'salary_x']]
