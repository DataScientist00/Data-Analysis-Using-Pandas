#problem link-->> https://platform.stratascratch.com/coding/10318-new-products?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df1 = car_launches[car_launches['year'] == 2019]
df2 = car_launches[car_launches['year'] == 2020]
df3 = df1.groupby('company_name')['product_name'].count().reset_index()
df4 = df2.groupby('company_name')['product_name'].count().reset_index()
df5 = pd.merge(df4,df3 , on = 'company_name')
df5['net_new_products'] = df5['product_name_x'] - df5['product_name_y']
df5[['company_name','net_new_products']]
