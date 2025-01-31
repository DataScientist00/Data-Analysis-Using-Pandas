#problem link-->> https://platform.stratascratch.com/coding/9805-find-drafts-which-contains-the-word-optimism?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
drafts = google_file_store[google_file_store['filename'].str.lower().str.startswith('draft')]

drafts[drafts['contents'].str.lower().str.contains('\s+optimism ')]
