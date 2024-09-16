#problem link-->> https://platform.stratascratch.com/coding/10048-top-businesses-with-most-reviews?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
yelp_business[['name','review_count']].nlargest(5 , 'review_count' , keep = 'first').sort_values('review_count',ascending=False)
