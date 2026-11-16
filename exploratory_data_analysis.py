import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from rich import print

sns.set_style("whitegrid")
sns.despine(left=True)
color = sns.color_palette('deep')
save_dir = 'Data/Raw data/visualizations'

subscriptions = pd.read_csv('Data/Raw data/subscriptions.csv')
usage = pd.read_csv('Data/Raw data/usage.csv')

#Replacing missing minutes_active values with 0 where workouts_completed is 0,
usage.loc[usage['workouts_completed'] == 0, ['minutes_active']] = usage.loc[usage['workouts_completed'] == 0, ['minutes_active']].fillna(0)
usage = usage.dropna()

missing_rows = (subscriptions['churned'] == 'yes') & (subscriptions['cancel_reason'].isna())
subscriptions.loc[missing_rows, 'cancel_reason'] = subscriptions.loc[missing_rows, 'cancel_reason'].fillna("not_specified")



