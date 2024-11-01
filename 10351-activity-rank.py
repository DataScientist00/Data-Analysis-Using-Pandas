#problem link-->> https://platform.stratascratch.com/coding/10351-activity-rank?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = google_gmail_emails.groupby('from_user')['id'].count().reset_index().rename(columns={'id':'total_emails'}).sort_values(['total_emails','from_user'],ascending=[False,True])
df['rank'] = df['total_emails'].rank(ascending=False , method='first')
df
