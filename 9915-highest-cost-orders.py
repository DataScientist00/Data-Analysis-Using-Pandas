#problem link-->> https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(customers,orders,how='inner' , left_on = 'id' , right_on = 'cust_id')
df1 = df.loc[df['order_date'].between('2019-02-01','2019-05-01')]
df2 = df1.groupby(['first_name','order_date'])['total_order_cost'].sum().reset_index()
df2.loc[df2['total_order_cost']==df2['total_order_cost'].max()]
