#problem link-->> https://platform.stratascratch.com/coding/9891-customer-details?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
temp = pd.merge(customers , orders , how ='left' , left_on = 'id' , right_on = 'cust_id')
temp = temp[['first_name' , 'last_name' , 'city', 'order_details']].sort_values(['first_name','order_details' ])
temp
