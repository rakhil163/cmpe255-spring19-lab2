#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:23:46 2019

@author: rakhil163
"""
def mean_num_friends(x):
    return sum(x)/len(x)

def median_num_friends(x):
    x.sort()
    if(len(x)%2==1):
        return (x[(len(x))//2])
    else:
        return ((x[(len(x)//2)-1]+x[(len(x))//2])/2)
        

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))