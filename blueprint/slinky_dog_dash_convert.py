import pandas as pd
import os

file_name = os.environ.get('file_name')
exported_file_name = os.environ.get('exported_file_name')

df = pd.read_csv(file_name)
df['SPOSTHR'] = round(df['SPOSTMIN'] / 60,2)
df.to_csv(exported_file_name,index = None)
