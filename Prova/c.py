import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')

csv['Sobrevivente'] = csv['Survived']
csv['Sobrevivente'] = csv['Sobrevivente'].replace([1],'Sim')
csv['Sobrevivente'] = csv['Sobrevivente'].replace([0],'Nao')

linhas = csv.head(10)
nomes = linhas.sort_values('Name')

print(nomes)