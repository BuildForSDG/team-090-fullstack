""" This populates City table with cities. 
"""

import csv
#from smartcity.models import MyCity

with open('data/worldcities.csv', encoding='utf8') as f:
    res = csv.reader(f)
    count = 0
    res = list(res)
    c = 0
    while c < 10:
        print(res[c])
        c +=1


    
 