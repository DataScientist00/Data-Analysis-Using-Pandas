#problem link-->> https://platform.stratascratch.com/coding/9845-find-the-number-of-employees-working-in-the-admin-department?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = worker[worker['department'] == 'Admin']
df['dd'] = df['joining_date'].dt.month
df[df['dd'] >= 4].count().drop_duplicates()
