#problem link-->> https://platform.stratascratch.com/coding/9913-order-details?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(customers,orders , left_on = 'id' ,right_on = 'cust_id')
df1=df[df['first_name']=='Jill'][['order_date','order_details','total_order_cost','first_name','id_x']].rename(columns={'id_x':'id1'})
df2=df[df['first_name']=='Eva'][['order_date','order_details','total_order_cost','first_name','id_y']].rename(columns={'id_y':'id1'})
pd.concat([df1,df2]).sort_values('id1').set_index('id1')
