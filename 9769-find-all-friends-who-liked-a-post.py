#problem link-->> https://platform.stratascratch.com/coding/9769-find-all-friends-who-liked-a-post?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
facebook_reactions.query("reaction == 'like'")[['friend']].drop_duplicates()
