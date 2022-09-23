Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> grade=input("enter the grade(A/B) :")
... salary= int(input("enter the salary :"))
... if (grade == 'A') and (salary>10000):
...     bonus= salary*(5/100)
...     print(" total salary is:", bonus+salary)
... elif (grade == 'B') and (salary>10000):
...     bonus= salary*(10/100)
...     print("total salary is:",bonus+salary)
... elif (grade == 'A') and (salary<=10000):
...     bonus= salary*(7/100)
...     print(" total salary is:",bonus+salary)
... elif (grade == 'B') and (salary<=10000):
...     bonus=salary*(12/100)
...     print("total salary is:",bonus+salary)
... else:
...     print("wrong input")
