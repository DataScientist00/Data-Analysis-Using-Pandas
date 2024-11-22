#problem link-->> https://platform.stratascratch.com/coding/9874-find-the-top-ten-hotels-with-the-highest-ratings?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
hotel_reviews['rank'] =  hotel_reviews['average_score'].rank(method='min', ascending=False)
hotel_reviews[hotel_reviews['rank']<=10][['hotel_name','average_score']].sort_values(by='average_score',ascending=False)
