#problem link-->>https://platform.stratascratch.com/coding/9667-count-users-that-speak-english-german-french-or-spanish?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
playbook_users[playbook_users['language'].isin(['english' , 'german' , 'french' ,'spanish'])]['user_id'].nunique()
