Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
459
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 20
20
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 8
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 8, '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 69, '__package__': None, 'x': 4761, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'x': 25, 'y': 600, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    y = (x * x) - x + z
NameError: name 'z' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    z = x + y * 5
NameError: name 'y' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    P = (x - 3)(y + z)
TypeError: 'int' object is not callable
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'P': 42900, 'x': 25, 'y': 75, '__name__': '__main__', 'z': 1875, '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais = 5
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
mans_mainigais = 459
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 45
mans_mainigais = 45
vai tu esi ievadijis skaitli: 45
vēl atmiņā ir mainīgais x = 2025
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 8.6549
mans_mainigais =      8.655
vai tu esi ievadijis skaitli:     8.6549
vēl atmiņā ir mainīgais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123456789.09
mans_mainigais = 123456789.090
vai tu esi ievadijis skaitli: 123456789.0900
vēl atmiņā ir mainīgais x = 15241578772412744.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123123123123
mans_mainigais = 123123123123.000
vai tu esi ievadijis skaitli: 123123123123.0000
vēl atmiņā ir mainīgais x = 15159303447561417785344.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'yolo' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123yolo4565

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1
    123yolo4565
              ^
SyntaxError: unexpected EOF while parsing
>>> type(x)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: harder daddy

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: s
mans_mainigais = s
vai tu esi ievadijis rindu: s

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 10, in <module>
    print("vēl atmiņā ir mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: ss
mans_mainigais = ss
vai tu esi ievadijis rindu: ss
>>> 
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
459
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 20
20
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 8
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 8, '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 69, '__package__': None, 'x': 4761, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'x': 25, 'y': 600, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    y = (x * x) - x + z
NameError: name 'z' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    z = x + y * 5
NameError: name 'y' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    P = (x - 3)(y + z)
TypeError: 'int' object is not callable
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'P': 42900, 'x': 25, 'y': 75, '__name__': '__main__', 'z': 1875, '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais = 5
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
mans_mainigais = 459
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 45
mans_mainigais = 45
vai tu esi ievadijis skaitli: 45
vēl atmiņā ir mainīgais x = 2025
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 8.6549
mans_mainigais =      8.655
vai tu esi ievadijis skaitli:     8.6549
vēl atmiņā ir mainīgais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123456789.09
mans_mainigais = 123456789.090
vai tu esi ievadijis skaitli: 123456789.0900
vēl atmiņā ir mainīgais x = 15241578772412744.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123123123123
mans_mainigais = 123123123123.000
vai tu esi ievadijis skaitli: 123123123123.0000
vēl atmiņā ir mainīgais x = 15159303447561417785344.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'yolo' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123yolo4565

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1
    123yolo4565
              ^
SyntaxError: unexpected EOF while parsing
>>> type(x)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: harder daddy

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: s
mans_mainigais = s
vai tu esi ievadijis rindu: s

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 10, in <module>
    print("vēl atmiņā ir mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: ss
mans_mainigais = ss
vai tu esi ievadijis rindu: ss
>>> 
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
459
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 20
20
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 8
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 8, '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 69, '__package__': None, 'x': 4761, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'x': 25, 'y': 600, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    y = (x * x) - x + z
NameError: name 'z' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    z = x + y * 5
NameError: name 'y' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    P = (x - 3)(y + z)
TypeError: 'int' object is not callable
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'P': 42900, 'x': 25, 'y': 75, '__name__': '__main__', 'z': 1875, '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais = 5
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
mans_mainigais = 459
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 45
mans_mainigais = 45
vai tu esi ievadijis skaitli: 45
vēl atmiņā ir mainīgais x = 2025
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 8.6549
mans_mainigais =      8.655
vai tu esi ievadijis skaitli:     8.6549
vēl atmiņā ir mainīgais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123456789.09
mans_mainigais = 123456789.090
vai tu esi ievadijis skaitli: 123456789.0900
vēl atmiņā ir mainīgais x = 15241578772412744.0000000
>>> 
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
459
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 20
20
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi vienu skaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 8
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 8, '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 69
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 69, '__package__': None, 'x': 4761, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'x': 25, 'y': 600, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    y = (x * x) - x + z
NameError: name 'z' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 1

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    z = x + y * 5
NameError: name 'y' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    P = (x - 3)(y + z)
TypeError: 'int' object is not callable
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'P': 42900, 'x': 25, 'y': 75, '__name__': '__main__', 'z': 1875, '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 5
mans_mainigais = 5
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 459
mans_mainigais = 459
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi vienu skaitli: 45
mans_mainigais = 45
vai tu esi ievadijis skaitli: 45
vēl atmiņā ir mainīgais x = 2025
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 8.6549
mans_mainigais =      8.655
vai tu esi ievadijis skaitli:     8.6549
vēl atmiņā ir mainīgais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123456789.09
mans_mainigais = 123456789.090
vai tu esi ievadijis skaitli: 123456789.0900
vēl atmiņā ir mainīgais x = 15241578772412744.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123123123123
mans_mainigais = 123123123123.000
vai tu esi ievadijis skaitli: 123123123123.0000
vēl atmiņā ir mainīgais x = 15159303447561417785344.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'yolo' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123yolo4565

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1
    123yolo4565
              ^
SyntaxError: unexpected EOF while parsing
>>> type(x)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: harder daddy

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: s
mans_mainigais = s
vai tu esi ievadijis rindu: s

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 10, in <module>
    print("vēl atmiņā ir mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: ss
mans_mainigais = ss
vai tu esi ievadijis rindu: ss
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123123123123
mans_mainigais = 123123123123.000
vai tu esi ievadijis skaitli: 123123123123.0000
vēl atmiņā ir mainīgais x = 15159303447561417785344.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1, in <module>
NameError: name 'yolo' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 123yolo4565

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainigais = input("Cienijamais lietotaj, ludzu ievadi daļskaitli: ")
  File "<string>", line 1
    123yolo4565
              ^
SyntaxError: unexpected EOF while parsing
>>> type(x)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi daļskaitli: 1
mans_mainigais =      1.000
vai tu esi ievadijis skaitli:     1.0000
vēl atmiņā ir mainīgais x =       1.0000000
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: yolo

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: harder daddy

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: s
mans_mainigais = s
vai tu esi ievadijis rindu: s

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 10, in <module>
    print("vēl atmiņā ir mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: ss
mans_mainigais = ss
vai tu esi ievadijis rindu: ss
>>> 

  GNU nano 2.5.3                                      File: dgr_20180925.py                                                                         Modified  


Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: harder daddy

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: x

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 4, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: s
mans_mainigais = s
vai tu esi ievadijis rindu: s

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 10, in <module>
    print("vēl atmiņā ir mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienijamais lietotaj, ludzu ievadi simbolu rindu: ss
mans_mainigais = ss
vai tu esi ievadijis rindu: ss
>>> 


