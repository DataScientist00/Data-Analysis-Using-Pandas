#problem lin-->> https://platform.stratascratch.com/coding/9897-highest-salary-in-department?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df1=employee.groupby("department")['salary'].max().reset_index().rename(columns = {'salary':'highest_salary'})
df2=pd.merge(employee,df1,on='department',how='inner')
df2[df2['salary'] == df2['highest_salary']][['department','first_name','salary']]
