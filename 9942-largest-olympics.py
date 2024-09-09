#problem link-->> https://platform.stratascratch.com/coding/9942-largest-olympics?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events.groupby(['games'])['id'].nunique(1).reset_index().rename(columns={'id':'athelete_count'}).sort_values('athelete_count').tail(1)
