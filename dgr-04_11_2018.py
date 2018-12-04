Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> original = "to be or not to be"
>>> key = 50
>>> type(original)
<class 'str'>
>>> original[0]
't'
>>> ord(original[0])
116
>>> bin(ord(original[0]))
'0b1110100'
>>> chr(116)
't'
>>> ord(original[0]) ^ key
70
>>> chr(ord(original[0]) ^ key)
'F'
>>> message = []
>>> for i in range(len(original)):
	message.append(chr(ord(original[i]) ^ key))

>>> massage
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    massage
NameError: name 'massage' is not defined
>>> message
['F', ']', '\x12', 'P', 'W', '\x12', ']', '@', '\x12', '\\', ']', 'F', '\x12', 'F', ']', '\x12', 'P', 'W']
>>> message = ""
>>> for i in range(len(original)):
	message = message + (chr(ord(original[i]) ^ key))

	
>>> message
'F]\x12PW\x12]@\x12\\]F\x12F]\x12PW'
>>> for i in range(len(original)):
	message = message + (chr(ord(original[i]) ^ key))

	
>>> message
'F]\x12PW\x12]@\x12\\]F\x12F]\x12PWF]\x12PW\x12]@\x12\\]F\x12F]\x12PW'
>>> result = ""
>>> for i in range(len(message)):
	result = result + (chr(ord(message[i]) ^ key1))

	
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    result = result + (chr(ord(message[i]) ^ key1))
NameError: name 'key1' is not defined
>>> key1 = 50
>>> for i in range(len(message)):
	result = result + (chr(ord(message[i]) ^ key1))

	
>>> result
'to be or not to beto be or not to be'
>>> result = ""
>>> for i in range(len(message)):
	result = result + (chr(ord(message[i]) ^ key1))

	
>>> result
'to be or not to beto be or not to be'
>>> original\

    
'to be or not to be'
>>> message = ""
>>> for i in range(len(original)):
	message = message + (chr(ord(original[i]) ^ key))

	
>>> message
'F]\x12PW\x12]@\x12\\]F\x12F]\x12PW'
>>> result = ""
>>> for i in range(len(message)):
	result = result + (chr(ord(message[i]) ^ key1))

	
>>> result
'to be or not to be'
>>> 
