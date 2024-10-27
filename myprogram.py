Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\s-A009-37.CAMPUS> py
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> i. 7+4
  File "<stdin>", line 1
    i. 7+4
       ^
SyntaxError: invalid syntax
>>> i. 7 + 4
  File "<stdin>", line 1
    i. 7 + 4
       ^
SyntaxError: invalid syntax
>>> 7 + 4
11
>>> (30 + 10) / 2
20.0
>>> 2 ** 3
8
>>> 7 > 5
True
>>> r=4
>>> r = 4
>>> area = 3.14159 * r * r
>>> rea
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rea' is not defined. Did you mean: 'area'?
>>> area
50.26544
>>> round(area,2)
50.27
>>> first_name = "Mary"
>>> last_name = "Brown"
>>> full_name = first_name + ' ' + last_name
>>> full_name
'Mary Brown'
>>> print(full_name)
Mary Brown
>>> len(full_name)
10
>>> a=5
>>> h=4
>>> area = (a*h)/2
>>> print(area)
10.0
>>> a=7
>>> b=12
>>> c=31
>>> result = (a+b+c)/3
>>> round(result,2)
16.67
>>> print(result)
16.666666666666668
>>> print(result,2)
16.666666666666668 2
>>> print(round(result,2))
16.67
>>>py myprogram.py
