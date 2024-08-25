#problem link-->> https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
orders['year']=orders['order_date'].dt.year
orders['month']=orders['order_date'].dt.month
df1=orders[orders['year'] == 2019]
df2=df1[df1['month'] == 3]
df2.groupby("cust_id").sum('total_order_cost').reset_index()[['cust_id','total_order_cost']].rename(columns={'total_order_cost':'revenue'})
