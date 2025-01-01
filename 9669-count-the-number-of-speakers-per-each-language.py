#problem link-->> https://platform.stratascratch.com/coding/9669-count-the-number-of-speakers-per-each-language?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
playbook_users.groupby('language').agg(size=('user_id','count')).reset_index().sort_values(by='size',ascending=False)
