>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> help(int)

>>> help(float)

>>> help(string)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    help(string)
NameError: name 'string' is not defined
>>> help(strings)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    help(strings)
NameError: name 'strings' is not defined
>>> help(help)
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |  
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
 |  
 |  Calling help() at the Python prompt starts an interactive help session.
 |  Calling help(thing) prints help for the python object 'thing'.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> help(d)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    help(d)
NameError: name 'd' is not defined
>>> d = 2+2
>>> d
4
>>> help(d)

>>> round(42013.439218)
42013
>>> round
<built-in function round>
>>> round(42013.345311231231312, 5)
42013.34531
>>> pow(3,3)
27
>>> pow(3,3,3)
0
>>> 16%3
1
>>> 3%16
3
>>> id(9)
4334561888
>>> id(-9)
140408738542672
>>> def convert_to_celsius(fahrenheit):
	return (fahrenheit-32) * 5 / 9

>>> help(convert_to_celsius)
Help on function convert_to_celsius in module __main__:

convert_to_celsius(fahrenheit)

>>> convert_to_celsius(80)
26.666666666666668
>>> # man kunne også have givet fahrenheit et variable og få det samme resultat, her får vi dog også en difitnition som er indkodet, som man fx kan bruge senere hen
>>> int(26.6666666668)
26
>>> round(26.66666668)
27
>>> first(3+3)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    first(3+3)
NameError: name 'first' is not defined
>>> first = 3
>>> first = 3+3
>>> first
6
>>> help(def)
SyntaxError: invalid syntax
>>> help(def)
SyntaxError: invalid syntax
>>> x=2*x return x
>>> 1
f(x + 1) + f(x + 2)
SyntaxError: invalid syntax
>>> def f(x) :
	x = 2 * x
	return x

>>> x = 1
>>> x = f(x + 1) + f(x + 2)
>>> x
10
>>> #Det er en længere process (kig evt. eksempel igennem i bogen). Det vigtgste er at forståe af værdien af x går igennem en længere proces, hvor den hele tiden får en ny værdi. Dette sker især grundet return x kodningen, hvor x først har en værdi på 1, så 2 grundet 2*1, så 3 grundet x nye værdi (2) og lægger det ind i f(2+1 = 3 --> osv osv, som til sidst ender ud i (f(4 + 6)
>>> f(x)
20
>>> f(x)*2
40
>>> f(x)*x
200
>>> 
>>> 
>>> get_weekday(3, 1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    get_weekday(3, 1)
NameError: name 'get_weekday' is not defined
>>> 3,4
(3, 4)
>>> (3,4)
(3, 4)
>>> round(3,4)
3
>>> round(3.4)
3
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> abs(3)
3
>>> abs(4,8)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    abs(4,8)
TypeError: abs() takes exactly one argument (2 given)
>>> abs(4.3312)
4.3312
>>> abs = 2
>>> abs
2
>>> abs(4)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    abs(4)
TypeError: 'int' object is not callable
>>> abs(abs+2)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    abs(abs+2)
TypeError: 'int' object is not callable
>>> abs(-2)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    abs(-2)
TypeError: 'int' object is not callable
>>> abs(3)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    abs(3)
TypeError: 'int' object is not callable
>>> abs(3.3)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    abs(3.3)
TypeError: 'int' object is not callable
>>> print('noter)
      
SyntaxError: EOL while scanning string literal
>>> print('noter')
noter
>>
