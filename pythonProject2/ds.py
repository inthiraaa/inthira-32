import pandas as pd
data = pd.read_csv('salary_dataset.csv')
print(data)
print(data.info())
print(data.describe())
print("mean age = " , data ['age'].mean())
print("mean gpa = " , data ['gpa'].mean())
print("mean salary =  ", data ['salary'].max())
print("mean experience =  ", data ['experience'].min())
print(data.head())
print(data.tail())
print(data.loc[20])
print(data['age'].unique())
dataAge26=data[data['age']==26]
print(dataAge26)