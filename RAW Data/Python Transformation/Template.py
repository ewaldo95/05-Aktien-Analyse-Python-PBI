import pandas as pd
import numpy as np


Mylink = '/Users/ewaldofischer/Desktop/Projekt/Data Analyst/Projekt Porfolio/Aktien Projekt/SAP.csv'
df = pd.read_csv(Mylink, delimiter=',', decimal='.') 



df['Delta_Open_Close'] =   df['Open'] - df['Close']

df['Delta_High_Low'] = df['High'] - df['Low']

#df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y')

df['Date'] = pd.to_datetime(df['Date'])


df['Period'] = df['Date'].dt.strftime('%m-%Y')

df['description'] = np.where(df['Delta_Open_Close'] > 0, 'Up', 'Down')

df['Sum Monat'] = df.groupby('Period')['Close'].transform('mean')

df = pd.DataFrame(df)


df.to_csv('/Users/ewaldofischer/Desktop/Projekt/Data Analyst/Projekt Porfolio/Aktien Projekt/SAP_export.csv', index=False, sep=';')


print(df)