Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> "don't"+'forget'+'to'+'conserve'+'water'
"don'tforgettoconservewater"
>>> 'the'*3
'thethethe'
>>> 'the'+3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    'the'+3
TypeError: Can't convert 'int' object to str implicitly
>>> 'the'*3+'beautiful'+'earth'
'thethethebeautifulearth'
>>> 2*'true'
'truetrue'
>>> a='save'
>>> b='the'
>>> c='planet'
>>> 'a'+'b'+'c'
'abc'
>>> print(a+B+c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(a+B+c)
NameError: name 'B' is not defined
>>> PRINT(a+b+c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    PRINT(a+b+c)
NameError: name 'PRINT' is not defined
>>> print(a+b+c)
savetheplanet
>>> a=4
>>> b='panda bears'
>>> 'a'+'b'
'ab'
>>> print('a'+'b')
ab
>>> print(str(a)+b)
4panda bears
>>> test='I love food'
>>> len('test')
4
>>> len('i love food')
11
>>> test='i love meet'
>>> test.upper9'i love meet')
SyntaxError: invalid syntax
>>> test.upper('i love meet')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    test.upper('i love meet')
TypeError: upper() takes no arguments (1 given)
>>> test.upper()
'I LOVE MEET'
>>> test.lower()
'i love meet'
>>> test.capilize()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    test.capilize()
AttributeError: 'str' object has no attribute 'capilize'
>>> test.capitalize()
'I love meet'
>>> test.swapcase()
'I LOVE MEET'
>>> test.replace("o",'i')
'i live meet'
>>> a='MEET'
>>> b="meet"
>>> c="Meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a!=b
True
>>> a!=c
True
>>> b!=c
True
>>> ==
SyntaxError: invalid syntax
>>> replace("=",'!')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    replace("=",'!')
NameError: name 'replace' is not defined
>>> test.replace('=','!')
'i love meet'
>>> test==
SyntaxError: invalid syntax
>>> test='='
>>> test.replace('=','!')
'!'
>>> a==b
False
>>> test='a==b'
>>> test.replace('=','!')
'a!!b'
>>> my_string='bananayellowthinkhatgreyBIGcalifornia314'
>>> meet_value[12:17]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    meet_value[12:17]
NameError: name 'meet_value' is not defined
>>> meet_value=[12:17]
SyntaxError: invalid syntax
>>> 
