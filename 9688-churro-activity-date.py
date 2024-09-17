#problem link-->> https://platform.stratascratch.com/coding/9688-churro-activity-date?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['facility_name'] == 'STREET CHURROS']
df[df['score'] < 95][['activity_date','pe_description']]
