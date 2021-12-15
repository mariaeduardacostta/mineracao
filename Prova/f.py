import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
csv['Sex'] = csv['Sex'].replace(['male'],'masculino')
csv['Sex'] = csv['Sex'].replace(['female'],'FEMININO')
linhas = csv.head(10)

print(linhas['Sex'])