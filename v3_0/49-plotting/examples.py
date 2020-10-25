# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:49:05 2017

@author: acbart
"""

import random
from math import sqrt
import matplotlib.pyplot as plt
#%%
values = [sqrt(max(min(random.normalvariate(50, 20), 100), 0))*10
          for x in range(1000)]

plt.hist(values)
plt.xlabel("Grades")
plt.xlim(0, 100)
plt.ylabel("Students")
plt.title("Distribution of Student Grades")
plt.show()
#%%
plt.hist([sqrt(max(min(random.normalvariate(50, 20), 100), 0))*10
          for x in range(1000)])
plt.show()
#%%
y = 0
items= []
for m in range(1000):
    y += random.normalvariate(1, 10)
    items.append(y)
plt.plot(items)
plt.show()

#%%
y = 0
x = 0
items= []
items2 = []
for m in range(1000):
    x = random.normalvariate(10, 5)
    y = random.normalvariate(20, 5)+x*2
    items.append(y)
    items2.append(x)
plt.scatter(items, items2)
plt.show()
#%%
plt.hist([0, 5, 7,
          35, 35,
          51, 53, 57,
          61, 64,
          82, 84, 84, 88],
    bins=10, align='mid', range=(0, 100))
plt.xticks([x*10 for x in range(11)], map(str, [x*10 for x in range(11)]))
plt.show()
#%%
data = [1, 4, 8, 16, 8, 24, 32]
plt.xlabel("Time (Days)")
plt.ylabel("Money (Dollars)")
plt.title("Money raised over Time")
plt.plot(data, marker='o')
plt.show()

#%%
exam1 = [40, 43, 55, 60, 52, 63, 74]
exam2 = [50, 55, 67, 72, 70, 70, 70]
plt.scatter(exam1, exam2)
plt.show()

#%%
plt.ylim(0, 10)
plt.plot([1, 2, 1, 3, 4])
plt.plot([3, 4, 4, 5, 6])
plt.show()