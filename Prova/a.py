import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
linhas = csv.head(10)

print(linhas)

