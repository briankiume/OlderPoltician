from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data = pd.read_json('Brazil.json', lines=True)
data.gender = data.gender.apply(lambda v: 1 if v == 'female' else 0)
df = data.copy()
df = df[['gender', 'id', 'name', 'birth_date']]
df.dropna(subset=['birth_date'], inplace=True)
df['year'] = df.birth_date.str[:4].astype(int)

date_today = date.today()
current_year = int(str(date_today)[:4])
df['current_year'] = current_year
df['age'] = df['current_year'] - df['year']

x = df.gender.values
y = df.age.values

plt.figure()
ax = plt.subplot()
plt.scatter(x, y)
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()






