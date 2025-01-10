#problem link-->> https://platform.stratascratch.com/coding/9685-companies-with-chinese-speakers?code_type=2

# Import your libraries
import pandas as pd

playbook_users.query("language == 'chinese'").groupby('company_id').agg(num = ('user_id' , 'count')).reset_index().query('num > 1')[['company_id']]
