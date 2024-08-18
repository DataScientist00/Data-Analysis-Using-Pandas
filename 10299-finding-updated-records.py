#problem link-->> https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2

# Import your libraries
import pandas as pd

#I Know it's not optimal , but i wanted to try all the functions that i recently learned so i took the long path

# Start writing code
temp = ms_employee_salary.groupby('id').max('salary')
temp1 = pd.merge(ms_employee_salary , temp , how ='inner', on='id',suffixes=('_x', '_y'))
temp1 = temp1[temp1['salary_x'] == temp1['salary_y']]
temp2= temp1.drop(columns=['salary_x','department_id_x'])
temp2 = temp2.rename(columns={'salary_y':'salary' , 'department_id_y':'department_id'})
temp2 = temp2[['id' , 'first_name','last_name','department_id','salary']]
temp2


