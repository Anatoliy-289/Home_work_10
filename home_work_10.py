import numpy as np 
import pandas as pd

df = pd.DataFrame({'whoAmI':['robot', 'human']})

df = df.melt(ignore_index=False).reset_index().pivot_table('variable', 'index', 'value', aggfunc='count').fillna(0)

print(df)
