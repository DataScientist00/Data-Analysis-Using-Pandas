#problem link-->>> https://platform.stratascratch.com/coding/9770-find-the-number-of-views-each-post-has?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
facebook_post_views.groupby('post_id').size().to_frame("n_views").reset_index().sort_values(by='post_id')
