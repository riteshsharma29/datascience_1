#!/usr/bin/python
# coding: utf-8 -*-

#pie plots are similar to stack plot only they certain point in time. Use to show percentage in share
#Titanic Male-Female Death/Survival ratio

from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("titanic_data.csv")
keys = df['Sex'].values
values = df['Survived'].values

male_live = []
female_live = []
male_died = []
female_died = []

for element in df.values:
    if element[4] == 'male' and element[2] == 1: male_live.append(1)
    if element[4] == 'female' and element[2] == 1: female_live.append(1)
    if element[4] == 'male' and element[1] == 0: male_died.append(1)
    if element[4] == 'female' and element[1] == 0: female_died.append(1)

slices = [len(male_live),len(female_live),len(male_died),len(female_died)]

activities = ['male_live','female_live','male_died','female_died']

cols = ['r','b','m','c','k','g','w','navy','khaki','pink']


plt.pie(slices,
    labels=activities,
    colors=cols,
    startangle=90,
    shadow=True,
    explode=(0,0,0,0), #0.1 is used to explote the slice-share use 0.0 instead if this feature is not required.
    autopct='%1.1f%%'	
)

plt.title('Titanic Male-Female Death/Survival ratio')

plt.show()
