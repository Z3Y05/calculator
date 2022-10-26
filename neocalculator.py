# -*- coding: utf'-8 -*-
"""
Created on Thu Jun  2 17:40:16 2022

@author: User
"""

import math
from colorama import Fore, Back, Style
m=input('what whould you like, addition (add),subtraction(sub),multiplicaation(mul),division(div), or loagarithm(log), fractions(fra)percentages(per)')

if(m == 'add'):
  x=float(input('first number:'))
  y=float(input('second number'))
  print(x+y)
elif(m == 'mul'):
  x=float(input('first number:'))
  y=float(input('second number:'))
  print(x*y)
elif(m == 'sub'):
  x=float(input('first number:'))
  y=float(input('second number:')) 
  print(x-y)
elif(m == 'div'):
 x=float(input('first number:'))
 y=float(input('second number:'))
 print(x/y)
elif(m == 'log'):
    x=float(input('base:'))
    y=float(input('second number:'))
    print(math.log(y,x))
elif(m== 'fra'): 
    x=float(input('numerator:'))
    y=float(input('denominator:'))    
    z=float(input('whole number:'))
    a=((x/y)*z)
    print(a)
elif(m=='per'):
    x=float(input('main number:'))
    y= float (input('_% of main number:'))
    quotient = x / y
    percent = quotient * 100
    print(percent)
else:
 print('error, retry')    
  
  