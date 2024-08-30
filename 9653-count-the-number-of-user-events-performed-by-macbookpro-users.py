#problem link-->> https://platform.stratascratch.com/coding/9653-count-the-number-of-user-events-performed-by-macbookpro-users?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
playbook_events[playbook_events['device']=='macbook pro'].groupby("event_name").size().reset_index()
