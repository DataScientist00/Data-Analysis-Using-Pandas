#problem link-->> https://platform.stratascratch.com/coding/9847-find-the-number-of-workers-by-department?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
worker[worker['joining_date'].dt.month >= 4].groupby(['department']).size().reset_index(name = 'num_workers').sort_values(by = 'num_workers', ascending = False)
