#problem link-->> https://platform.stratascratch.com/coding/10077-income-by-title-and-gender?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
total_bonus = sf_bonus.groupby("worker_ref_id")["bonus"].sum().reset_index()
df = pd.merge(sf_employee , total_bonus , left_on = "id" , right_on = "worker_ref_id" , how = "left")
df.dropna(subset=['bonus'] , inplace = True)
df['total'] = df['salary'] + df['bonus']
df.groupby(['employee_title' , 'sex'])['total'].mean().reset_index()
