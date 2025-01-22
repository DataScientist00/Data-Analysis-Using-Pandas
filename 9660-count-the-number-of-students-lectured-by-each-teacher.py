#problem link-->> https://platform.stratascratch.com/coding/9660-count-the-number-of-students-lectured-by-each-teacher?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
sat_scores.groupby('teacher').size().reset_index()
