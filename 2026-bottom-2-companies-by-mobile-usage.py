#problem link-->> https://platform.stratascratch.com/coding/2026-bottom-2-companies-by-mobile-usage?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = fact_events.query("client_id == 'mobile'").groupby('customer_id').agg(n_events = ('event_id','count')).reset_index()
df['rank'] = df['n_events'].rank(method = 'min' , ascending = True)
df.query('rank <= 2')[['customer_id' , 'n_events']]
