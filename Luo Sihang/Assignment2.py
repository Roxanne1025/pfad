
from io import StringIO
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

url="https://datashareclub.com/area/%E7%A6%8F%E5%BB%BA/%E5%8E%A6%E9%97%A8.html"
response = requests.get(url)

if response.ok:
    print("Data is ready")

    soup = bs(response.text, 'html.parser')
    table = soup.find('table') 

tables_tr = str(table)

table_io = StringIO(tables_tr)

df = pd.read_html(table_io,header=1)[0]

df=df.values

data=[]

for row in df:
    
    index,time, weather, temperture = row[:4] 
    data.append((time, temperture))

# print(data)

df = pd.DataFrame(data, columns=['Date','temperture'])
year=2024

df['Date'] = df['Date'].apply(lambda x: f'{year}-{x}')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M')
df.set_index('Date', inplace=True)
df['temperture'] = df['temperture'].str.replace('℃', '').astype(float)


plt.figure(figsize=(10, 5))
plt.plot(df.index, df['temperture'], marker='o', linestyle='-', color='b')

plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')

plt.grid(True)

plt.show()