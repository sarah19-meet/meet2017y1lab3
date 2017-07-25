Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 5+3
8
>>> my_string='bananayellowthinkhatBIGcalifornia314'
>>> my_string[12:17]
'think'
>>> my_string[12:17]+[20:14]
SyntaxError: invalid syntax
>>> my_string[12:17+20:14]
'ti'
>>> my_string[12:17]+my_string[20:24]
'thinkBIGc'
>>> my_string[12:17]+my_string[20:23]
'thinkBIG'
>>> my_string=meet_value
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_string=meet_value
NameError: name 'meet_value' is not defined
>>> meet_value=my_string
>>> meet_value=my_string[12:17]+my_string[20:13]
>>> meet_value=my_string[12:17]+my_string[20:23]
>>> print(meet_value)
thinkBIG
>>> meet_value.upper()
'THINKBIG'
>>> 
