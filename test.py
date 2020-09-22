# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:21:35 2020

@author: Faisal Mangi
"""

import json 
  
# Opening JSON file 
with open('source_file_2.json') as json_file: 
    data = json.load(json_file) 
  
    # for reading nested data [0] represents 
    # the index value of the list 
    print(data['managers'][0]) 
      
    # for printing the key-value pair of 
    # nested dictionary for looop can be used 
    print("\nPrinting nested dicitonary as a key-value pair\n") 
    for i in data['mangers']: 
        print("Name:", i['name']) 
        print("Website:", i['website']) 
        print("From:", i['from']) 
        print() 