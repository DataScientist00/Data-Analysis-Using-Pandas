#problem link-->> https://platform.stratascratch.com/coding/9892-second-highest-salary?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
employee['rank'] = employee['salary'].rank(method='dense',ascending=False)
employee[employee['rank'] == 2]['salary'].drop_duplicates()
