#problem link-->> https://platform.stratascratch.com/coding/9766-find-the-complaint-id-for-the-processed-complaints-of-type-1?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
facebook_complaints[(facebook_complaints['processed'] == True) & (facebook_complaints['type'] == 1)][['complaint_id']]
