#problem link-->> https://platform.stratascratch.com/coding/10064-highest-energy-consumption?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
df=pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])
df1 =df.groupby("date").sum().reset_index().sort_values('consumption',ascending=False)
a = df1['consumption'].max()
df1[df1['consumption'] ==a]
