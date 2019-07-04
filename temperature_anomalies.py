import pandas as pd

data = pd.read_csv("Book1.csv", na_values=-9999)
# print(data)
data = data.drop([0])
# print(data)

number = data['TAVG'].isnull().sum()
notnull = data.__len__() - number
print("Not Null values in TAVG : ", notnull)

number2 = data['TMIN'].isnull().sum()
notnull2 = data.__len__() - number2
print("Not Null Values in TMIN : ", notnull2)

days = len(data['DATE'])
print("no. of days :", days)

first_date = data['DATE'][1]
print("First date : ", first_date)

last_date = data['DATE'][days]
print("Last date : ", last_date)

tavg_int = []
data2 = data.dropna(subset=['TAVG'])
for i in data2['TAVG']:
    tavg_int.append(int(i))
data2['TAVG'] = tavg_int
avg_temp = data2['TAVG'].mean()
print("Average temp of whole data : ", avg_temp)

data3 = data.dropna(subset=['TMAX'])
list1 = []
list2 = data3['TMAX'].values
count =0
for i in data3['DATE']:
    if (i[:6] == '196905') or (i[:6]=='196906') or (i[:6]=='196907') or (i[:6]=='196908'):
        list1.append(int(list2[count]))
    count+=1
print("max temp in summer of 69 : " , max(list1))


