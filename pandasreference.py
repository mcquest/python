"""
mcquest notes on
https://pandas.pydata.org/docs/user_guide/10min.html
"""

# import libraries for statistics and data analysis
import numpy as np
"""
np.random.randint(0,7, size=10)
"""
import pandas as paneldata

print("hello  world~", "\n")#testing environment print statement

# panel data is a table // matrix

#  a series is one column
s = paneldata.Series([1, 3, 5, np.nan, 6, 8])
print(s,"\n")

# create a range of dates
dates = paneldata.date_range("20330101", periods=6)
print(dates, "\n")

# a data frame  is a table-chart
dtafrme1 = paneldata.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(dtafrme1, "\n")

"""
    distribution
    >>> np.random.randn
    dimensional list with returned samples 
    from 'standard normal' distribution
"""

#custom dataframe
dtafrme2 = paneldata.DataFrame(
    {
       "A1": 1.0,
       "BDate": paneldata.Timestamp("20230102"),
       "Cfloat": paneldata.Series(2, index=list(range(4)), dtype="float32"),
       "Dint": np.array([3] * 4, dtype="int32"),
       "Etagories": paneldata.Categorical(["test","train","stretch","yes"]),
       "F00": "placeholder",
    }
)
print(dtafrme2, "\n")

# custom dataframe
dtafrme3 = paneldata.DataFrame([[0, 2, 3], [0, 4, 1], [10,20,30]],
                               index= [4,5,6], columns=list("ABC"))
print(dtafrme3, "\n\n", dtafrme3.at[4,'B'], "\n\n")



"""
    pandas- panel data reference functions
    >>> .head(), .tail(int for how many rows) 
    >>> .dtypes, .index, .columns 
    
    >>> .decribe(), .to_numpy(), .copy()
    .dropna() #drop rows w/ missing data
    .fillna(value=), .isna()
    >>> .sort_index(axis=, ascending=boolean)
    >>> .sort_values(by="{column_name}")
    
    .at[row, column] -> return a value  (iat for integer)
    .loc[row] -> return a row (iloc for integer)
    
    >>> .isin() for  filtering
    # ex: df2[df2["E"].isin(["two", "four"])] -> rows where  column E  is  two or four
    # ex: df[df > 0] -> return values above 0
    # ex: select data based on values from a single column
    
    >>> .apply(function to column)
    
    s.str.lower()
    
    add columns to DataFrames not rows
        pass in to it  a pre-built list of records
        
    pd.merge(SQL style)
    
    [79]left = pd.DataFrame({"key": ["placeholder", "placeholder"], "lval": [1, 2]})

    [80]right = pd.DataFrame({"key": ["placeholder", "placeholder"], "rval": [4, 5]})

    left
    Out[79]: 
        key  lval
        0  placeholder     1
        1  placeholder     2

    right
    Out[80]: 
        key  rval
        0  placeholder     4
        1  placeholder     5

    pd.merge(left, right, on="key")
    Out[81]: 
        key  lval  rval
        0  placeholder     1     4
        1  placeholder     1     5
        2  placeholder     2     4
        3  placeholder     2     5
    
    or if l,r 1 is 'name' then  
    Out[86]: 
        key     lval   rval
        0  placeholder     1     4
        1  name     2     5
"""

# Grouping 
print("\n\n")#statement for human visualization spacing
# placeholder and name are placeholder names 
dtafrme4 = paneldata.DataFrame(
    {
            "A": ["placeholder", "name", "placeholder", "name", "placeholder", "name", "placeholder", "placeholder"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.random.randn(8),
    }
)
print(dtafrme4, "\n\n")
# grouping  same  A values & add CD values 
print(dtafrme4.groupby("A")[["C","D"]].sum())
# group same A && B values
print(dtafrme4.groupby(["A","B"]).sum())
