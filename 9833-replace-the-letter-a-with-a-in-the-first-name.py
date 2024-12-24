#problem link-->> https://platform.stratascratch.com/coding/9833-replace-the-letter-a-with-a-in-the-first-name?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
worker['first_name'].str.replace('a','A').rename('replace_a')
