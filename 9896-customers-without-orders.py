#problem link-->> https://platform.stratascratch.com/coding/9896-customers-without-orders?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
cust_ord = pd.merge(customers , orders , left_on = 'id', right_on = 'cust_id' , how = 'left' , suffixes = ('_c'  , '_o'))

cust_ord[cust_ord['id_o'].isnull() == True][['first_name']]
