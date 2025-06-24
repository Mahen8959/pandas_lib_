import pandas as pd
#DataFrame

# a=pd.DataFrame({'Yes':[1,2],'No':[3,4]})
# print(a)

# b=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A","B","C"],index=["x","y","z"])
# print(b)
# print(b.head(2))
# print(b.tail(2))
# print(b.index)
# print(b.columns)
# print(b.info())
# print(b.describe())
# print(b.nunique())
# print(b['A'].unique())
# print(b.shape)
# print(b.size)

#Loading in DataFrame from Files
coffee=pd.read_csv('Pandascode/pandas_lib_/data.csv')
print(coffee)
