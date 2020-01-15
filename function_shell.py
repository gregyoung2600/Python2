Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:\Users\gregy\Music\Python2\functions.py =============
What is your name? greg
>>> name
'greg'
>>> def add(x,y):
	x + y

	
>>> add(5,10)
>>> def add(x,y):
	return x + y

>>> add(5,100)
105
>>> answer = add(100,20)
>>> answer
120
>>> def add(x,y)
SyntaxError: invalid syntax
>>> def add(x,y):
	print(x + y)

	
>>> add(100,50)
150
>>> answer = add(5,100)
105
>>> answer
>>> type(answer)
<class 'NoneType'>
>>> def add(x,y,z)
SyntaxError: invalid syntax
>>> def add(x,y,z):
	add(5,10,5)

	
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def add(x,y,z):
	return x + y + z
add
SyntaxError: invalid syntax
>>> 
>>> add(5,10,5)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    add(5,10,5)
  File "<pyshell#24>", line 2, in add
    add(5,10,5)
  File "<pyshell#24>", line 2, in add
    add(5,10,5)
  File "<pyshell#24>", line 2, in add
    add(5,10,5)
  [Previous line repeated 991 more times]
RecursionError: maximum recursion depth exceeded
>>> def add(x,y)
SyntaxError: invalid syntax
>>> def add(c,t):
	return c + t

>>> add(10,10)
20
>>> add(40,40)
80
>>> def add(r,z):
	return r + z

>>> add(10,29)
39
>>> word = "dictionary"
>>> word[::-1]
'yranoitcid'
>>> rev = input("Put in some text.")
Put in some text.
>>> rev
''
>>> rev
''
>>> print(rev)

>>> print "rev"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("rev")?
>>> rev
''
>>> this is my text
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> def rev(text):
	return text[::-1]

>>> rev("apple")
'elppa'
>>> def jack(text):
	return jack[::-1]
jack("what")
SyntaxError: invalid syntax
>>> jack("candy")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    jack("candy")
NameError: name 'jack' is not defined
>>> def rev(jack):
	return jack[::-1]

>>> jack("candy")
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    jack("candy")
NameError: name 'jack' is not defined
>>> def
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> def rev(green):
	return green[::-1]

>>> rev("bacon")
'nocab'
>>> def rev(house):
	return house[::-1]

>>> rev("nobody")
'ydobon'
>>> rev(100,101,102,103)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    rev(100,101,102,103)
TypeError: rev() takes 1 positional argument but 4 were given
>>> rev([100,101,102,103])
[103, 102, 101, 100]
>>> 
