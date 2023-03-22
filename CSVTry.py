import pandas as pd
import random
import secrets
data = pd.read_csv(r'C:\Users\GAV-GAV\Downloads\ages.csv')
df = pd.DataFrame(data)
data2 = ['a','dd','k']
print(data2[secrets.randbelow(3)])