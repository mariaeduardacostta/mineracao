import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv('titanic.csv')
file=pd.ExcelWriter('excel.xlsx')
csv.to_excel(file, index = False)
file.save()