#problem link-->> https://platform.stratascratch.com/coding/10046-top-5-states-with-5-star-businesses?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business[yelp_business['stars'] == 5]
df.groupby('state').count().reset_index()[['state','business_id']].sort_values(['business_id','state'] , ascending = [False,True]).nlargest(5 , columns = 'business_id', keep = 'all')
