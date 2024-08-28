#problem link-->> https://platform.stratascratch.com/coding/9905-highest-target-under-manager?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = salesforce_employees.loc[salesforce_employees['manager_id']==13]
df.loc[df['target'] == df['target'].max() , ['first_name','target'] ]

