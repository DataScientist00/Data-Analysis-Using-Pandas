#problem link-->> https://platform.stratascratch.com/coding/10166-reviews-of-hotel-arena?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df =hotel_reviews[hotel_reviews['hotel_name'] == 'Hotel Arena']
df.groupby(['hotel_name','reviewer_score'])['review_date'].count().reset_index().rename(columns={'review_date':'n_reviews'})
