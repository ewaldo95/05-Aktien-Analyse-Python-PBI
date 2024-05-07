import pandas as pd
import numpy as np


MyLink = '/Users/ewaldofischer/Desktop/Projekt/Data Analyst/Projekt Porfolio/Aktien Projekt/IBM.csv'

df = pd.read_csv(MyLink, delimiter = ',' , decimal= '.')

df['Date'] =  pd.to_datetime(df['Date'])


df['Delta_Open_Close'] = df['Open'] - df['Close'] 

df['Delta_High_Low'] = df['High'] - df['Low']

df['Date'] = pd.to_datetime(df['Date'])

df['Period'] = df['Date'].dt.strftime('%m-%Y')

df['description'] = np.where(df['Delta_Open_Close'] > 0, 'Up', 'Down')


df['Sum Monat'] = df.groupby(df['Period'])['Close'].transform('mean')

df = pd.DataFrame(df)

df.to_csv('/Users/ewaldofischer/Desktop/Projekt/Data Analyst/Projekt Porfolio/Aktien Projekt/IBM_Export.csv', index= False, sep=';')

print(df)