# -*- coding: utf-8 -*-
"""beautifulSoup.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L5nOQYppIJCgiip6mJZpOMjkVUC5ZxtF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#url = "http://www.hubertiming.com/results/2017GPTR10K"
url = "https://www.hubertiming.com/results/2023WyEasterLong"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
print(type(soup))

title = soup.title
print(title)

rows = soup.find_all('tr')
print(rows[:10])

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = re.sub(clean, '', str_cells)
    list_rows.append(clean2)
print(clean2)
print(type(clean2))

df = pd.DataFrame(list_rows)
df.head(10)

df1 = df[0].str.split(',', expand=True)
df1[0] = df1[0].str.strip('[')
df1.head(10)

col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)

df2 = pd.DataFrame(all_header)
df2.head()

df3 = df2[0].str.split(',', expand=True)
df3.head()

frames = [df3, df1]
df4 = pd.concat(frames)
df4.head(10)

df5 = df4.rename(columns=df4.iloc[0])
df5.head()

df6 = df5.dropna(axis=0, how='any')
df6.info()
print(df6.shape)

df7 = df6.drop(df6.index[0])
df7.head()

df7.rename(columns={'[Place': 'Place'}, inplace=True)
df7.rename(columns={' Team]': 'Team'}, inplace=True)
df7.head()
df7.columns = df7.columns.str.strip().str.replace('[\[\]]', '', regex=True)
df7.head()

time_list = df7['Time'].tolist()
time_mins = []
for i in time_list:
    parts = i.split(':')
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h = 0
        m, s = parts
    minutes = (int(h) * 3600 + int(m) * 60 + int(s)) / 60
    time_mins.append(minutes)
df7['Runner_mins'] = time_mins
df7.head()

print(df7.describe(include=[np.number]))
from pylab import rcParams
rcParams['figure.figsize'] = 15, 5
df7.boxplot(column='Runner_mins')
plt.grid(True, axis='y')
plt.ylabel('Chip Time')
plt.xticks([1], ['Runners'])
plt.title("Boxplot of Runner Finish Times")
plt.show()

x = df7['Runner_mins']
ax = sns.distplot(x, hist=True, kde=True, rug=False, color='m', bins=25, hist_kws={'edgecolor':'black'})
plt.title("Distribution of 10K Runner Finish Times")
plt.show()

# Plot distributions for male and female runners
f_fuko = df7.loc[df7['Gender'] == ' F']['Runner_mins']
m_fuko = df7.loc[df7['Gender'] == ' M']['Runner_mins']
sns.distplot(f_fuko, hist=True, kde=True, rug=False, hist_kws={'edgecolor': 'black'}, label='Female')
sns.distplot(m_fuko, hist=False, kde=True, rug=False, hist_kws={'edgecolor': 'black'}, label='Male')
plt.legend()
plt.show()

g_stats = df7.groupby("Gender", as_index=True).describe()
print(g_stats)

df7.boxplot(column='Runner_mins', by='Gender')
plt.ylabel('Chip Time')
plt.suptitle("")
plt.title("Boxplot of Runner Finish Times by Gender")
plt.show()