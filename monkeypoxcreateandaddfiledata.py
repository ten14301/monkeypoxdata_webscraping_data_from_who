import pandas as pd
import requests
import csv


url = 'https://raw.githubusercontent.com/owid/notebooks/main/EdouardMathieu/monkeypox/owid-monkeypox-data.csv'
proxies = {}
response = requests.get(url=url, proxies=proxies)
with open("response.csv", "wb") as f:
    f.write(response.content)

df = pd.read_csv('response.csv')
dfchoose = pd.DataFrame(df,columns=['location','date'])
print(dfchoose)
dfchoose.to_csv("output.csv", sep='\t', encoding='utf-8')
dfaa = dfchoose.groupby(["location"]).count()
print(dfaa)



