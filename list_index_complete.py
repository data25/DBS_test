# -*- coding: utf-8 -*-
"""
Question 3: Find the different persons
@author: Thiru Nadesan
"""

import pandas as pd
import time

store_list=[]
overall_list=[]

#problem definition
data = [("Thiru", 212, "thiru@python.com"),
        ("guess", 212, "xxx@python.com"),
        ("James", 444, "james@python.com"),
        ("mate", 1024, "thiru@python.com"),
        ("vivek", 894, "vivek@python.com"),
        ("none", 894, "none@python.com"),
        ("humpty", 444, "humpty@python.com"),
        ("dumpty", 444, "dumpty@python.com"),
        ("PhD", 521, "dumpty@python.com"),
        ("chandola", 931, "chandola@python.com"),
        ("grumpy", 8, "chandola@python.com")]

#convert to DataFrame
t1=time.time()
df = pd.DataFrame(data, columns = ['Name', 'phone', 'email'])

col_list = df.columns.tolist() #get the column names

for i in range(df.shape[0]):
    compare_list = df.loc[i,:]
    for col in col_list:
        list_dict = df.index[df[col]==compare_list[col]].tolist()
        store_list.append(list_dict)

while True:
    comp_list = store_list[0]
    indices=[]
    for i in range(len(store_list)):
        if bool(set(store_list[i]) & set(comp_list)):
            comp_list = list(set(comp_list+store_list[i]))
            indices.append(i)
    
    overall_list.append(list(set(comp_list)))
    overall_list = list(map(list,set(map(tuple,overall_list))))
    
    for j in sorted(indices, reverse=True):
        del store_list[j]
    
    
    if not store_list:
        break

t2 = time.time()
print("There are {} different persons : {}".format(len(overall_list), overall_list))
print("Execution time is {} seconds".format(t2-t1))