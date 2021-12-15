import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
csv = csv.drop(columns=['SibSp'])
csv = csv.drop(columns=['Parch'])
csv = csv.drop(columns=['Ticket'])
linhas = csv.head(10)

print(linhas)