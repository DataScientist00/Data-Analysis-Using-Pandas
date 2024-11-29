#problem link-->> https://platform.stratascratch.com/coding/2127-sales-revenue?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
amazon_sales[amazon_sales['order_date'].dt.year == 2021]['order_total'].sum()
