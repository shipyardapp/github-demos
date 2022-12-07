import pandas as pd
df = pd.read_csv('disney_world_wait_times/slinky_dog_dash.csv')
df['SPOSTHR'] = round(df['SPOSTMIN'] / 60,2)
df.to_csv('disney_world_wait_times/slinky_dog_dash_with_hours.csv',index = None)
