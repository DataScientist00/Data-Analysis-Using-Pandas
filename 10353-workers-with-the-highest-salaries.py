#problem link-->> https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(worker , title , left_on='worker_id' , right_on = 'worker_ref_id')

df[df['salary'] == df['salary'].max()]['worker_title']
