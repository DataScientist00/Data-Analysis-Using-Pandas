#problem link-->> https://platform.stratascratch.com/coding/2058-total-shipment-weight?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment['total_weight']=amazon_shipment.groupby('shipment_id')['weight'].transform('sum')
amazon_shipment

