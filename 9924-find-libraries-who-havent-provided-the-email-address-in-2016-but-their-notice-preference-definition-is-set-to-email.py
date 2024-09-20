#problem link-->> https://platform.stratascratch.com/coding/9924-find-libraries-who-havent-provided-the-email-address-in-2016-but-their-notice-preference-definition-is-set-to-email?tabname=question&code_type=2


# Import your libraries
import pandas as pd

# Start writing code
library_usage[(library_usage['circulation_active_year'] == 2016) & (library_usage['notice_preference_definition'] == 'email') & (library_usage['provided_email_address'] == False) ]['home_library_code'].drop_duplicates()
