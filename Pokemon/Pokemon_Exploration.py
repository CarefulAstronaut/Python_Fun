# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:16:39 2020

@author: Mitch
@Git: github.com/CarefulAstronaut
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Questions to be asked:
    1) Which type of Pokemon has the highest base attack speed?
    2) Is one type of Pokemon more likely to have a secondary?
    3) Does the type diversification change with generations?
    4) Which generation was the strongest?
"""

data = pd.read_csv("Python_Fun/Pokemon/Pokemon_Data.csv")
data = data.drop(data.columns[0], axis = 1)

# Figure 1 - count of pokemon in each generation

gen_labels = ['Gen1', 'Gen2', 'Gen3', 'Gen4', 'Gen5', 'Gen6']
gencount = data.groupby('Generation').count().iloc[:, 0]

x = np.arange(len(gen_labels)) # the label locations
width = 0.35 # the width of the bars

fig, ax = plt.subplots()
rect1 = ax.bar(x, gencount, width, label='Unique Pokemon Count')

ax.set_ylabel('Count')
ax.set_title('Pokemon Count by Generation')
ax.set_xticks(x)
ax.set_xticklabels(gen_labels)
ax.legend()

fig.tight_layout()

plt.show()

# Figure 2 - Type/Subtype Diversity in each generation

gentype1_x = data.groupby(['Generation', 'Type 1']).count().iloc[:, 0].reset_index()
gentype1_pivot = gentype1_x.pivot(index='Generation', columns='Type 1', values='Name').fillna(0)
gentype2_x = data.groupby(['Generation', 'Type 2']).count().iloc[:, 0].reset_index()
gentype2_pivot = gentype2_x.pivot(index='Generation', columns='Type 2', values='Name').fillna(0)
gentype_pivot = gentype1_pivot + gentype2_pivot
gentype_labels = gentype_pivot.columns

x1 = np.arange(len(gentype_labels))
width1 = 0.2

fig1, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)

ax1.bar(x1, gentype_pivot.iloc[0, :], width1)
ax1.set(title='Count of Pokemon by Type/Subtype (Gen 1)')
ax1.set_xticks(x1)
ax1.set_xticklabels(gentype_labels)

ax2.bar(x1, gentype_pivot.iloc[1, :], width1)
ax2.set(title='Count of Pokemon by Type/Subtype (Gen 1)')

ax3.bar(x1, gentype_pivot.iloc[2, :], width1)
ax3.set(title='Count of Pokemon by Type/Subtype (Gen 1)')

ax4.bar(x1, gentype_pivot.iloc[3, :], width1)
ax4.set(title='Count of Pokemon by Type/Subtype (Gen 1)')

ax5.bar(x1, gentype_pivot.iloc[4, :], width1)
ax5.set(title='Count of Pokemon by Type/Subtype (Gen 1)')

ax6.bar(x1, gentype_pivot.iloc[5, :], width1)
ax6.set(title='Count of Pokemon by Type/Subtype (Gen 1)')



plt.show()

# Extra Code


gentype1 = gentype1_x.groupby('Generation').count().iloc[:, 0]


gentype2 = gentype2_x.groupby('Generation').count().iloc[:, 0]



rect2 = ax.bar(x, gentype1, width, label='Pokemon Type Count')
rect3 = ax.bar(x + width, gentype2, width, label='Pokemon Subtype Count')

def autolabel(rect):
    """Attach a text label above each bar in *rects*, displaying height"""
    for rect in rect:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width(), height),
                    xytext(0, 3), 
                    textcoords="offset points",
                    ha='centre', va='bottom')