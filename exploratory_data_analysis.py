import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from rich import print

subscriptions = pd.read_csv('data/subscriptions.csv')
usage = pd.read_csv('data/usage.csv')

#Random samples from each DataFrame.
#print(subscriptions.sample(10))

print(subscriptions.isna().sum())
print(usage.isna().sum())


