problem link-->> https://platform.stratascratch.com/coding/9814-counting-instances-in-text?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = google_file_store['contents'].str.lower().str.split().explode().value_counts().reset_index()
df1 = df[(df['index'] == 'bull') | (df['index'] == 'bear')]
df1.rename(columns = {'index':'word' , 'contents':"netry"})
