#problem link-->> https://platform.stratascratch.com/coding/9632-host-popularity-rental-prices?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
result=airbnb_host_searches[['price','room_type','host_since','zipcode','number_of_reviews']]
result.drop_duplicates(inplace=True)
def Rating(x):
     if x==0:
         return 'New'
     elif x>=1 and x<=5:
        return 'Rising'
     elif x>=6 and x<=15:
        return 'Trending Up'
     elif x>=16 and x<=40:
        return 'Popular'
     else:
        return 'Hot'
result['popularity']=result['number_of_reviews'].apply(Rating)
result.groupby('popularity')['price'].agg(['mean','min','max']).reset_index()
