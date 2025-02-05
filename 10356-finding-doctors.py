#problem libk-->>>https://platform.stratascratch.com/coding/10356-finding-doctors?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
employee_list[(employee_list['profession'].str.lower() == 'doctor')&(employee_list['last_name'].str.lower() == 'johnson')][['first_name','last_name']]
