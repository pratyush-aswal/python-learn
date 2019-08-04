import pandas as pd

df = pd.read_csv(r"F:\F\python\weather_data_cities.csv")
# print(df)
gb = df.groupby('city')
for city_name, city_df in gb:
    print(city_name)
    print(city_df)
print("groupbycity----------------" * 5)
a = gb.get_group('paris')
print(a)
print("----------------" * 5)
print(a.max(),'nn')
print("----------------" * 5)
print(a.describe())
print("----------------" * 5)
print(gb.describe())
print("----------------" * 5)

df1 = pd.DataFrame({'city': ['a', 'b', 'c', 'd'], 'temp': [65, 70, 30, 34]})
print(df1)
df2 = pd.DataFrame({'city': ['d', 'u', 't', 'q'], 'temp': [1, 2, 4, 6]})

print("concat----------------" * 5)
df_new = pd.concat([df2, df1])
print(df2 + df1)
print("plus----------------" * 5)
print(df_new)
print("ignore----------------" * 5)
df_new = pd.concat([df2, df1], ignore_index=True)
print(df_new)
print("axis----------------" * 5)
df_new = pd.concat([df2, df1], axis=1)
print(df_new)

print("tempmerge----------------" * 5)
temp_df = pd.DataFrame({'city': ['q', 'w', 'e', 'r'], 'temp': [1, 2, 3, 4]})
humidity_df = pd.DataFrame({'city': ['q', 'w', 'e', 'd'], 'temp': [9, 8, 7, 6]})
x = pd.merge(temp_df, humidity_df, on='city')
print(x)

print("outermerge----------------" * 5)
x = pd.merge(temp_df, humidity_df, on='city', how='outer')
print(x)

print("num.index----------------" * 5)
numdf = pd.DataFrame(['z', 'x', 'c', 'v'], index=[29, 30, 44, 5])
print(numdf)

print("row_ind_iloc/loc----------------" * 5)
x = numdf.iloc[1]
y = numdf.loc[29]
print(y)
print(x)

print("row_slice----------------" * 5)
print(numdf.iloc[:3])
print('-=-=')
print(numdf.loc[30:5])
