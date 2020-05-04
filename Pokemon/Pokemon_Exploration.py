# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:16:39 2020

@author: Mitch
@Git: github.com/CarefulAstronaut
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Python_Fun.Pokemon.Spider_Plot import radar_factory

"""
Potential Questions to be asked:
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

# DUPLICATE CODE - LOOP??
gentype1_x = data.groupby(['Generation', 'Type 1']).count().iloc[:, 0].reset_index()
gentype1_pivot = gentype1_x.pivot(index='Generation', columns='Type 1', values='Name').fillna(0)
gentype2_x = data.groupby(['Generation', 'Type 2']).count().iloc[:, 0].reset_index()
gentype2_pivot = gentype2_x.pivot(index='Generation', columns='Type 2', values='Name').fillna(0)
gentype_pivot = gentype1_pivot + gentype2_pivot
gentype_pivot.sum().sort_values(ascending=False).iloc[:6]

gentype_top6 = gentype_pivot.loc[:, ['Water', 'Normal', 'Flying', 'Grass', 'Psychic', 'Bug']]

width1 = 0.2

fig1, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
fig1.set_size_inches(12.0, 10.0)

# DUPLICATE CODE - LOOP?
ax1.bar(x, gentype_top6.iloc[:, 0], width1)
ax1.set(title='Count of Water Pokemon by Gen')
ax1.set_xticks(x)
ax1.set_xticklabels(gen_labels)

ax2.bar(x, gentype_top6.iloc[:, 1], width1)
ax2.set(title='Count of Normal Pokemon by Gen')
ax2.set_xticks(x)
ax2.set_xticklabels(gen_labels)

ax3.bar(x, gentype_top6.iloc[:, 2], width1)
ax3.set(title='Count of Flying Pokemon by Gen')
ax3.set_xticks(x)
ax3.set_xticklabels(gen_labels)

ax4.bar(x, gentype_top6.iloc[:, 3], width1)
ax4.set(title='Count of Grass Pokemon by Gen')
ax4.set_xticks(x)
ax4.set_xticklabels(gen_labels)

ax5.bar(x, gentype_top6.iloc[:, 4], width1)
ax5.set(title='Count of Psychic Pokemon by Gen')
ax5.set_xticks(x)
ax5.set_xticklabels(gen_labels)

ax6.bar(x, gentype_top6.iloc[:, 5], width1)
ax6.set(title='Count of Bug Pokemon by Gen')
ax6.set_xticks(x)
ax6.set_xticklabels(gen_labels)

plt.show()

# Figure 3 - Subtype Counts 
df4_x = data.iloc[:, :3]
df4_y1 = df4_x.drop(['Type 2'], axis=1).groupby('Type 1').count().sort_values(by='Name', ascending=False)
df4_y2 = df4_x.drop(['Type 1'], axis=1).groupby('Type 2').count().sort_values(by='Name', ascending=False)

fig3, (ax1, ax2) = plt.subplots(figsize=(9, 9), nrows=1, ncols=2)
ax1.pie(df4_y1.values, labels=df4_y1.index, startangle=90, autopct='%1.1f%%')
ax1.axis('equal')

ax2.pie(df4_y2.values, labels=df4_y2.index, startangle=90, autopct='%1.1f%%')
ax2.axis('equal')

plt.show()

# Figure 4 - Subtype Average Base Stats by Gen
## Ran into an issue here where 'FLYING' is only a Type 2 trait; will ignore for now
top4 = ['Water', 'Normal', 'Grass', 'Psychic']

df3_x = data.loc[data['Type 1'].isin(top4)].drop(['Total', 'Legendary', 'Name', 'Type 2'], axis=1)
df3_x = df3_x.groupby(['Type 1', 'Generation']).mean()
df3_y = df3_x / df3_x.max()
df3_y = df3_y.reset_index()

stats = [['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
for x in top4:
    group = [x]
    test = []
    dummy = df3_y.loc[df3_y['Type 1'] == x]    
    for i in range(6):
        num = dummy.iloc[i, 2:].to_list()
        test.append(num)
    group.append(test)
    group = tuple(group)
    stats.append(group)
    
    
N = 6
theta = radar_factory(N, frame='polygon')
spoke_labels = stats.pop(0)

fig3, axs = plt.subplots(figsize=(9, 9), nrows=2, ncols=2, 
                         subplot_kw=dict(projection='radar'))
fig3.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

colors = ['b', 'r', 'g', 'm', 'y', 'gold']

# Plot the five types on separate axes
for ax, (title, case_data) in zip(axs.flat, stats):
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
    ax.set_ylim(0)
    ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                 horizontalalignment='center', verticalalignment='center')
    for d, color in zip(case_data, colors):
        ax.plot(theta, d, color=color)
        ax.fill(theta, d, facecolor=color, alpha=0.25)
    ax.set_varlabels(spoke_labels)

# add legend relative to top-left plot
labels = gen_labels
legend = axs[0, 0].legend(labels, loc=(0.9, .95),
                          labelspacing=0.1, fontsize='small')

fig.text(0.5, 0.965, 'Relative Average Base Stats Among Generations',
         horizontalalignment='center', color='black', weight='bold',
         size='large')

plt.show()