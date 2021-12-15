import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
csv = csv.head(20)
csv['Survived'].fillna(0,inplace=True)
csv.drop(csv.loc[csv['Survived'] == 0].index,inplace=True)
csvG = csv.groupby('Pclass', as_index = False)['Survived'].count()

print(csvG)