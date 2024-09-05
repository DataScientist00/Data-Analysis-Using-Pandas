#problem link-->> https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(facebook_reactions , facebook_posts , on = 'post_id')
df[df['reaction'] == 'heart'][['post_id','poster_y','post_text','post_keywords' , 'post_date']].drop_duplicates()

