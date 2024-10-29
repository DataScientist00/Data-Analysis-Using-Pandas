#problem link--> https://platform.stratascratch.com/coding/514-marketing-campaign-success-advanced?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
marketing_campaign['rank_1'] = marketing_campaign.groupby('user_id')['created_at'].rank(method='dense')
marketing_campaign['rank_2'] = marketing_campaign.groupby(['user_id','product_id'])['created_at'].rank(method='dense')
df=marketing_campaign[marketing_campaign['rank_1'] > 1]
final = df[df['rank_2'] == 1]
len(final['user_id'].unique())
