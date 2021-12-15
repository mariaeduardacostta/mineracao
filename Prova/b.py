import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
linhas = tita.head(10)
nomes = linhas.sort_values('Name')

print(nomes)