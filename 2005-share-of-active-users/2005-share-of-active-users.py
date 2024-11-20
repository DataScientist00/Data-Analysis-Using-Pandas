#problem link-->> https://platform.stratascratch.com/coding/2005-share-of-active-users/solutions?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = len(fb_active_users.query('status=="open" and country =="USA"')) / len(fb_active_users.query('country=="USA"'))
df1 = {'open':[df]}
pd.DataFrame(df1)
