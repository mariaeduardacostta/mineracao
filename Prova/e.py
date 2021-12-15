import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
csv = csv.drop(columns=['SibSp'])
csv = csv.drop(columns=['Parch'])
csv = csv.drop(columns=['Ticket'])
renomeado = csv.rename(columns = {'PassengerId': 'IdPassageiro', 'Survived': 'Sobrevivnetes', 'Pclass':'ClasseP', 'Name':'Nome','Sex':'Sexo', 'Age':'Idade', 'Fare':'Tarifa', 'Cabin':'Cabine', 'Embarked':'Embarcou'}, inplace = False)
linhas = renomeado.head(10)

print(linhas)