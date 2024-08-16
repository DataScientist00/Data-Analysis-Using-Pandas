#problem link--->> https://platform.stratascratch.com/coding/9917-average-salaries?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
temp = employee[["department","salary"]].groupby("department").mean("salary")
temp2 = employee[["department","first_name","salary"]]
temp3 = temp2.merge(temp , how ='inner' , on ='department')
temp3
