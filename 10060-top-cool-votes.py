#problem link-->> https://platform.stratascratch.com/coding/10060-top-cool-votes?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.loc[yelp_reviews['cool'] == yelp_reviews['cool'].max(),  ['business_name','review_text']]
