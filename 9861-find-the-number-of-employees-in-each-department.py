#problem link-->> https://platform.stratascratch.com/coding/9861-find-the-number-of-employees-in-each-department?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
worker.groupby('department').agg(num_of_workers=('worker_id','count')).reset_index()
