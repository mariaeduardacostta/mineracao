import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
csv['Survived'].fillna(0,inplace=True)
csv.drop(csv.loc[tita['Survived'] == 0].index,inplace=True)
final = csv.groupby('Pclass', as_index = False)['Survived'].count()
plt.bar(final['Pclass'], final['Survived'])
plt.show()

print(final)