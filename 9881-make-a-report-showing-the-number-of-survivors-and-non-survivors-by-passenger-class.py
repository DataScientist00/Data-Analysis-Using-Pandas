#problem link-->> https://platform.stratascratch.com/coding/9881-make-a-report-showing-the-number-of-survivors-and-non-survivors-by-passenger-class?code_type=2


# Import your libraries
import pandas as pd

# Start writing code
df = titanic.groupby(['pclass' , 'survived'])['passengerid'].count().reset_index()
pd.pivot_table(df , index = 'survived',columns='pclass',values='passengerid').reset_index().rename(columns={1:'first_class',2:'second_class',3:'third_class'})
