# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:28:37 2020

@author: Mitchell Rea
@MMM UID: A7HN3ZZ
@Github: https://github.com/CarefulAstronaut
"""

"""
Project was inspired by the post "Minimally Sufficient Pandas" (linked below).  I'm familiar with some of 
these concepts but not others.  The post goes over the pros and cons of each style/syntax, but I'll just be
using what is suggested in the  post.  The list below covers the examples I'll be practicing. 

Selecting a single column of data
The deprecated ix indexer
Selection with at and iat
read_csv vs read_table duplication
isna vs isnull and notna vs notnull
Arithmetic and Comparison Operators and their Corresponding Methods
Builtin Python functions vs Pandas methods with the same name
Standardizing groupby aggregation
Handling a MultiIndex
The similarity between groupby, pivot_table and crosstab
pivot vs pivot_table
The similarity between melt and stack
The similarity between pivot and unstack
"""

import pandas as pd

df = pd.read_csv("Play/api.csv")

# Selecting a single column of data - Use bracket notation over dot notation
df['regionname']

# The deprecated ix indexer
df.iloc[:100, 2:7]  # 'integer' location; rowx, then columns
df.loc[:100, ['regionname', 'countryname', 'lendinginstr']]  # location; rows, then columns

# Selection with at and iat


# read_csv vs read_table duplication
# isna vs isnull and notna vs notnull
# Arithmetic and Comparison Operators and their Corresponding Methods
# Builtin Python functions vs Pandas methods with the same name
# Standardizing groupby aggregation
# Handling a MultiIndex
# The similarity between groupby, pivot_table and crosstab
# pivot vs pivot_table
# The similarity between melt and stack
# The similarity between pivot and unstack
