import pandas as pd
import os

# cwd = os.getcwd()

# Load Movie Dataset (subset)
df = pd.read_csv("D:\Movie Recommender\data\main-data\movies_metadata.csv", low_memory=False)

pd.set_option('display.max_columns', None)
print(df.head(5))
print(df.info())

# Drop 'homepage' column
df.drop(['homepage'], axis=1, inplace=True)

