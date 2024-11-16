#problem link--->>>> https://platform.stratascratch.com/coding/2119-most-lucrative-products?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = online_orders[(online_orders['date'].dt.month <= 6) & (online_orders['date'].dt.year == 2022) ]
df['total'] = df['cost_in_dollars'] * df['units_sold']
df.groupby('product_id').sum(['total']).reset_index().sort_values(by='total',ascending=False).head(5)[['product_id','total']]
