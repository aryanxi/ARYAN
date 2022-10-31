from time import time 
import random 
import os
from psutil import users 
from secrets import choice


x=int(input("ENTER THE NUMBER :"))
y=int(input("ENTER THE SECOND NUMBER :"))

def calc():

 print("choose your operater")
 userChoie=input("[+],[-],[*]:")
 if userChoie=='-':
    print(x-y)

 elif userChoie=='+':
     print(x+y)
    
 elif userChoie=='*':
     print(x*y)
     
 else:
    print('Choose the correct operator')
calc()

