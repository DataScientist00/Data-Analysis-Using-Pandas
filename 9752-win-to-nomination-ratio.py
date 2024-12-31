#problem link-->> https://platform.stratascratch.com/coding/9752-win-to-nomination-ratio?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
oscar_nominees.groupby('nominee').agg(ratio=('winner','mean')).reset_index().sort_values(by='ratio' ,ascending=False)
