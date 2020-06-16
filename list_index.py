# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:28:51 2020
This program outputs the indices of different person ids.
@author: tsltn
"""
import pandas as pd

overall_list=[]

#problem definition
data = [("Thiru", 212, "thiru@python.com"),
        ("guess", 212, "xxx@python.com"),
        ("James", 444, "james@python.com"),
        ("mate", 1024, "thiru@python.com")]

#convert to DataFrame
df = pd.DataFrame(data, columns = ['Name', 'phone', 'email'])

col_list = df.columns.tolist() #get the column names
index_list=df.index.tolist() #get the index list

list_dict={} #dictionary to store various compared results within the dataframe
for i in range(df.shape[0]):
    compare_list = df.loc[i,:]
    for col in col_list:
        list_dict[col+str(i)] = df.index[df[col]==compare_list[col]].tolist()

common_list=[]
single_list=[]
for k, v in list_dict.items():
    if len(v)>1:
        common_list.append(v)
    else:
        single_list.append(v)

common_list = list(set([item for l in common_list for item in l]))
single_list = list(set([item for l in single_list for item in l]))

if len(common_list)>len(single_list):
    diff = list(set(common_list) - set(single_list))
else:
    diff = list(set(single_list) - set(common_list))

overall_list.append(common_list)
overall_list.append(diff)
print(overall_list)