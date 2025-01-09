#problem link-->>> https://platform.stratascratch.com/coding/2057-weight-for-first-shipment?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment['earliest'] = amazon_shipment.groupby('shipment_id')['shipment_date'].transform('min')
amazon_shipment[amazon_shipment['shipment_date'] == amazon_shipment['earliest']][['shipment_id' , 'weight']]
