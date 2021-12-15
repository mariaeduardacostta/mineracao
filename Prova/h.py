import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
csv['Survived'].fillna(1,inplace=True)
csv.drop(csv.loc[tita['Survived'] == 1].index,inplace=True)
final = csv.groupby('Sex', as_index = False)['Survived'].count()

print(final)