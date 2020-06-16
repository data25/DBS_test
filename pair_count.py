# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 08:38:48 2020
"K difference Pair counting - Question 2"
@author: Thiru Nadesan
"""

import itertools
result_pair=[]

def pairs_count(input_list, n, K):
    ''' variables:
        input_list: integer; user input list
        n : integer; combination
        K : signed integer; Difference for which the pair has to be formed
    '''
    global result_pair
    
    pairs = list(itertools.combinations(input_list,n))
    
    for pair in pairs:
        if abs(pair[0]-pair[1]) == abs(K):
            result_pair.append(pair)
    
    return result_pair, K
            

if __name__=="__main__":
    input_list = [1, 5, 3, 4, 2, 20, 50, 55, 60, 75, 21]
    res, K = pairs_count(input_list, 2, 2)
    if not res:
        print("There is no pair that can be generated with the difference {}, from the list"
              .format(K))
    else:
        print("We will have {} pairs {}".format(len(res), res))