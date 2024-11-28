#problem link-->> https://platform.stratascratch.com/coding/2100-salary-by-education?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
google_salaries.groupby('education').agg(salary=('salary','mean')).reset_index()
