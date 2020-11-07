# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Hello World")
# if (conditionals): ******************
a=2
print(a)
if a==1:
    c=1
    b=1
elif a>2:
    c=2
    b=2
else:
    b=3
print(b)
# Loops: *******************************
acc=0
for x in range(1,10,3):
    acc=x+acc
    print(acc)
# Lists: ********************************
f=[]
print(f)
c=[
   'a',
   'v',3];
c.append(5)
print(c)
c.insert(0,'L')
print(c)
c.remove('v')
print(c)
del c[0]
print(c)
for y in c:
    print(y)
# Dictionaries ***************************
import pandas as pd
d= {"name":["Ali","Hojjat"],"address":"Uni DR"}
print(d['name'])
display(pd.DataFrame(d))
if 'name' in d:
    print('d has name')
print(d.keys())
print(d.values())
print(list(d.keys()))
# Advanced lists:
a= [1,2,3,4,5]
b= [5,6,7,8,9]
print(zip(a,b))
print(list(zip(a,b)))
for x,y in zip(a,b):
    print(f'x*y={x*y}')
a=['one','two','three','four','five']
print(list(enumerate(a)))
for idx,item in enumerate(a):
    print(f'index:{idx} holds "{item}"')
lst=[x*10 for x in range(0,20,2)]
print(lst)
lookup={key:value for value,key in enumerate(a)}
print(lookup)
print(lookup["two"])
# File Handling:
import pandas as pd
df = pd.read_csv("data\iris.csv")
print(df.head(5))
print('*****************')
display(df[0:5])
# functions:
def say_hello(speaker, person_to_greet, greeting = "Hello"):
    print(f'{greeting} {person_to_greet}, this is {speaker}.')
say_hello('Jeff', "John")
say_hello('Ali', "John", "Goodbye")
# a function that returns something:
def mu20(a):
    t=a*20
    return t
d=mu20(10)
print(d)
# mapping a function to a list:
L=[2,1,6,7,-1]
x=list(map(mu20,L)) # method1
y=[mu20(w) for w in L] # method2
print(x,y)
# filter definition:
def greater_than_5(x):
    return x>5
L5=list(filter(greater_than_5,L))
print(L5)
# Lambda definition (unnamed function):
L2=list(filter(lambda x: x<2,L))
Lp2=list(map(lambda x: x**2+1,L))
# and Reduce:
from functools import reduce
sumL=reduce(lambda x,y: x+y,L)
print(L2,Lp2,sumL)