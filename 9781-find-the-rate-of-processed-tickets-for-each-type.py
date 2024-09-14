#problem link-->> https://platform.stratascratch.com/coding/9781-find-the-rate-of-processed-tickets-for-each-type?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = facebook_complaints.groupby('type' , as_index = False)['processed'].mean()
