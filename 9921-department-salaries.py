#problem link-->> https://platform.stratascratch.com/coding/9921-department-salaries?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
employee.groupby(['department','sex']).agg(id=('id','count') , salary=('salary' , 'sum')).unstack(level='sex').reset_index()
