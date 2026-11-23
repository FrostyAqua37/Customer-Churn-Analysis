import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from rich import print

sns.set_style("whitegrid")
sns.despine(left=True)
color = sns.color_palette('deep')
save_dir = 'data/raw data/visualizations'

subscriptions = pd.read_csv('data/raw data/subscriptions.csv')
usage = pd.read_csv('data/raw data/usage.csv')



