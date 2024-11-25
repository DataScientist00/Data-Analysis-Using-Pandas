#problem link-->> https://platform.stratascratch.com/coding/2056-number-of-shipments-per-month?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment['shipment_date'] = amazon_shipment['shipment_date'].dt.strftime('%Y-%m')
amazon_shipment['key'] = amazon_shipment['shipment_id'].astype('str') + amazon_shipment['sub_id'].astype('str')
amazon_shipment.groupby('shipment_date')['key'].count().reset_index().rename(columns={'key':'count'})
