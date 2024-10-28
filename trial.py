import pandas as pd
df=pd.read_csv('C:\Program Files\Python312\wedding_data.csv')
df=pd.read_excel('C:\Users\SNEHA SINGH\Downloads\wedding_data.xslx.xlsx')
print(df.shape)
print(df.dtypes)
print(df.head())  # First few rows
print(df.tail())  # Last few rows
print(df.columns)
print(df['date'].unique())
print(df['date'].value_counts())
print(df.isnull().sum())
print(df.describe())
import matplotlib.pyplot as plt
df['date'].hist()
plt.show()
df.boxplot()
plt.show()
