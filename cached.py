# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:29:05 2020
Code for "Least Recently Used" Cache - hashmap 
@author: tsltn
"""
import time

class Cache(object):
    
    def __init__(self, maxmem):
        '''initializing the variables
        "mamxmem" (integer) is the maximum cache memory
        "cache" (dictionary) key-value pair that caches the inputs
        "lru" (dictionary) key-value pair that stores least recently
        used input
        "ttrace" counter for number of times the inputs has occurred
        '''
        self.maxmem = maxmem
        self.cache = {}
        self.lru = {}
        self.ttrace = 0
    
    '''function to check if the key already exists'''
    
    def get(self, key):
        if key in self.cache: #if key exists in the cache
            self.lru[key] = self.ttrace
            self.ttrace+=1
            #print("cached ... ")
            return self.cache[key]
        else:
            return -1
    
    '''function to delete when the maximum memory is reached
    and adds if the instances are new'''
    
    def set(self, key, val):
        if len(self.cache)>self.maxmem:
            least = min(self.lru.keys(), key = lambda k : self.lru[k])
            
            #print("popping the least recently used ...")
            self.cache.pop(least)
            self.lru.pop(least)
        else:
            self.cache[key] = val
            self.lru[key] = self.ttrace
            self.ttrace+=1
        
        #print("LRU: {}".format(self.lru))
        #print("CACHE: {}".format(self.cache))

def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        data = cache.get(n)
        if data==-1:
            res = fibo(n-1)+fibo(n-2)
            n = cache.set(n, res) #setting the key-value pair for the unoccurred instance
            return res
        else:
            return data # return the value if it exists in the cache
    
if __name__ == "__main__":
    n = 1000 # numbers till which the fibonacci series will be calculated
    cache = Cache(50) # initializing the cache capacity
    t1=time.time()
    fibo = fibo(n) #calling fibo function
    t2=time.time()
    print(fibo)
    print("Execution time is {}".format(t2-t1)+" seconds")
    
    
