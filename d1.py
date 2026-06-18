Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
    #python is an interpreted language
>>> s = "Aarya Musale"
>>> print s
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> s = "Aarya Musale"
... print (s)
SyntaxError: multiple statements found while compiling a single statement
>>> s = "Aarya Musale"
>>> s
'Aarya Musale'
#string is immutable in python(it wont make changes in original object)
In python data type we have 2 ops
1 mutable
2 immutable


#diff ops for python coding
#1. IDLE
#2. PyCharm IDE
#3. VS code
#4. Google colab

#but which to use?
#-> VS code becoz it is a Microsoft product,trustworthy one.


#Identifier - a name give to the object.These are also called as variables.
#Object - is a physical entity present in the program/memory


#Rules of declaring an identifier
#1. a-z A-Z allowed
#2. _ underscore is allowed
#3. special symbols and characters are not allowed except _
#4. number as a prefix not allowed
  #  eg. 2_pin = 1234 (not allowed)
#5. number as suffix is allowed
 #   eg. num1 =100(allowed)
#6. don't use reserve keywords
 #   eg. in = 99
#to check reserve keywords we have keyword libraryIdentifier - a name give to the object.These are also called as variables.
#Object - is a physical entity present in the program/memory

>>> s.capitalize()
'Aarya musale'
>>> s.upper()
'AARYA MUSALE'
>>> s
'Aarya Musale'
