Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
... Type "help", "copyright", "credits" or "license()" for more information.
... #python string assignment
... 
... 
... #how do you concatenate two strings in python ?
... """we can use the +operator to concatenate two strings directly by placing them together"""
... 'we can use the +operator to concatenate two strings directly by placing them together'
... 
... string1="fistr"
... string2="assignment"
... result=string1+""+string2
... print(result)
... fistrassignment
... 
... 
... 
... #what is the difference between the + operator and the join () method for concatenating two strings?
... """+operator is used to concatenate strings directly placing them together"""
... '+operator is used to concatenate strings directly placing them together'
... string1=haseeb"
... SyntaxError: unterminated string literal (detected at line 1)
... string1="haseeb"
... string2="ansari"
... result=string1+""+string2
... print(result)
... haseebansari
... 
... 
... """join method is used for concatenating multiple strings from an lists"""
... 'join method is used for concatenating multiple strings from an lists'
... 
... my_list=["haseeb""world"]
... result="".join(my_list)
... print(result)
... haseebworld
... 
... 
... 
... #how do you access individual characters in a string?
... 
... """we can access individual characters in a string by using indexing"""
... 'we can access individual characters in a string by using indexing'
... 
... string1="python"
print(string1[3])
h
print(string1[1])
y



"""by using negative indexing"""
'by using negative indexing'

string1="python"
print(string1[-3])
h
prnt(string1[-5])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    prnt(string1[-5])
NameError: name 'prnt' is not defined. Did you mean: 'print'?
print(string1[-5])
y


"""by using slicing in a string"""
'by using slicing in a string'

string1=python
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    string1=python
NameError: name 'python' is not defined
string="python"
print(string[2:4])
th


string1="python"
print(string1[-2:-4])

print(string1[-1:-3])

print(string1[2:5])
tho



#what method is use to find the lenght of a string
string="python"
print(len"string"))
SyntaxError: unmatched ')'



string="haseeb ansari"
lenght=len(string)
print("lenght of string:")
lenght of string:


string="i am learning python")
SyntaxError: unmatched ')'
string=("i am learning python")
n=len(string)
print(n)
20


string=("delhi is the capital of india")
n=len(string)
print(n)
29


'''by using len () function we can find the lenght of the string'''
'by using len () function we can find the lenght of the string'




#how do u convert a string to upper case and to lower case ?

my_string="Did you have a good day today?"
uppercse_string=my_string.upper()
print(uppercase_string)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print(uppercase_string)
NameError: name 'uppercase_string' is not defined. Did you mean: 'uppercse_string'?
my_string="did you have a good day"
uppercase=my_string.upper()
print(uppercase)
DID YOU HAVE A GOOD DAY


my_string="I AM LEARNING PYTHON"
lowwercase=my_string.lower()
lowwercase=my_string.lower()
print(lowwercase)
i am learning python


#what method is used to replace a substring with in a string



string="Nothing is impossible to a willing heart."
new_string=original_string.replace("heart""person")
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    new_string=original_string.replace("heart""person")
NameError: name 'original_string' is not defined
string="sky is blue"
new_string=string.replace("blue""grey")
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    new_string=string.replace("blue""grey")
TypeError: replace expected at least 2 arguments, got 1
string="sky is blue"
print(string.replace("blue","grey")


      string="sky is blue"
print(string.replace("blue","grey")
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
string="sky is blue"
print(string.replace("blue","grey"))
      
SyntaxError: multiple statements found while compiling a single statement
string="hello python"
      
print(string.replace("hello","hey"))
      
hey python
string="hello universe"
      
print(string.replace("universe","world"))
      
hello world


#how can you split a string in to a list of substrings based on a delimetere ?
      
string="hello python how are you"
      
list1=string.split()
      
print(list1)
      
['hello', 'python', 'how', 'are', 'you']


string= "the world is full of colours"
      
list=string.split()
      
print(list)
      
['the', 'world', 'is', 'full', 'of', 'colours']



#how do you check if a ttring starts with a particular substring?
      
string="python is interpreted language"
      
string1=string.startswith("python"))
      
SyntaxError: unmatched ')'
string="python is interpreted language"
      
string1=string.startswith("python")
      
SyntaxError: multiple statements found while compiling a single statement
string="python is interpreted language"
      
string1=string.startswith("python")
      
SyntaxError: multiple statements found while compiling a single statement
string="python is interpreted language"
      
string1=string.startswith("python"))
SyntaxError: multiple statements found while compiling a single statement
string="python is interpreted language"
      
string.startswith("python")
SyntaxError: multiple statements found while compiling a single statement




string1="hello the world of programming"
print(string1.startswith("hello"))
True



string2="my name is haseeb"
print(string2.starts_with("haseeb"))
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    print(string2.starts_with("haseeb"))
AttributeError: 'str' object has no attribute 'starts_with'. Did you mean: 'startswith'?
string2="my name is haseeb"
print(string2.startswith("haseeb"))
SyntaxError: multiple statements found while compiling a single statement
string1="hello python"
print(string1.startswith("haseeb"))
False

print(string1.endswith("world"))
False


#how can you removeleading and trailing whitespace from a string?


string1="000//hi, how are you"
newstring=string1.strip()
print(newstring)
000//hi, how are you
 s="\thi how r u?\n"
 
SyntaxError: unexpected indent
string1="  hi how r u"
new_string=string1.strip()
print(new_string)
hi how r u



string1="   \my name is haseeb"
newstr=string1.strip()
print(string1)
   \my name is haseeb





s="    hi name is haseeb"
>>> news=s.strip()
>>> printh(news)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    printh(news)
NameError: name 'printh' is not defined. Did you mean: 'print'?
>>> print(news)
hi name is haseeb
>>> 
>>> 
>>> 
>>> #what method is used to find the index of the first occurence of a substring with in a string
>>> 
>>> 
>>> string1="haseeb"
>>> string="the quick brown fox jumps over the lazy dog"
>>> index=string.index("over")
>>> print(index)
26
>>> 
>>> 
>>> string="the quick brown fox jumps over the lazy dog"
... index=string.index("24")
SyntaxError: multiple statements found while compiling a single statement
>>> string="the quick brown fox jumps over the lazy dog"
>>> index=string.index("23")
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    index=string.index("23")
ValueError: substring not found
>>> string="the quick brown fox jumps over the lazy dog"
... index=string.find("over")
SyntaxError: multiple statements found while compiling a single statement
>>> string="my name is haseeb"
>>> index=string.find("fox")
>>> 
>>> string="my name is haseeb"
... index=string.find("fox")
SyntaxError: multiple statements found while compiling a single statement
>>> string="my name is haseeb"
... index=string.find("name")
SyntaxError: multiple statements found while compiling a single statement
>>> string1="hey python"
>>> index=string1.find("python")
>>> print(index)
4


#how can you count the number of occurence of a substring with in a string?

my_string="a quck brown fox jumps over brown a lazy dog"
count=my_string.count("brown")
print(count)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers


my_string="hello, hello , hello, hello"
substring="hello"
count=my_string.count(substring)
print(f"'{substring}'appears{count}times in the string.")
'hello'appears4times in the string.



my_string="a quick brown brown fox jumps"
substring="brown"
count=my_string.count(substring)
print(f"'{substring}appears{count}times in a string.")
'brownappears2times in a string.








#how do you check if a string is contains only alphabetical charachters or numeric characters?


my_string="haseeb ansari"
alphabetic=my_string.isalpha()
print(f"is{my_string}'alphabetic?{is_alphabetic}")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(f"is{my_string}'alphabetic?{is_alphabetic}")
NameError: name 'is_alphabetic' is not defined. Did you mean: 'alphabetic'?


string="haseeb ansari"
slphabetic=string.isalpha()
print(f"is'{string}'alphabetic?{slphabetic}")
is'haseeb ansari'alphabetic?False


string="hellopython"
alphabetic=string.isalphabetic()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    alphabetic=string.isalphabetic()
AttributeError: 'str' object has no attribute 'isalphabetic'




string="haseebansari"
alphabetic=string.isalpha()
print(f"is'{string}'alphabetic?{alphabetic}")
is'haseebansari'alphabetic?True



#if a string is conntain only a numeric characters?

string=125688
numeric=string.isnum
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    numeric=string.isnum
AttributeError: 'int' object has no attribute 'isnum'


string=158225
numeric=string.isdigit()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    numeric=string.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'


string"1246"
SyntaxError: invalid syntax


string="125488"
numeric=string.isdigit()
print(f"is;{string}'numeric?{numeric}")
is;125488'numeric?True





#how can you check that if a string is a pelindrome?


#how can we reverse a string in python ?


string="haseeb ansari"
reversed=string[::-1]
print("Reversedstring:",reversed)
Reversedstring: irasna beesah



string="a lion in the jungle"
reversed=string[::-1]
print("Reversedstring:",reversed)
Reversedstring: elgnuj eht ni noil a




#how do you format a string with placeholders for variable value?


name=haseeb
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    name=haseeb
NameError: name 'haseeb' is not defined


Name="haseeb"
Age="27"
formatted_string="My name is {} and i am {} years old.".for(Name,Age)
SyntaxError: invalid syntax



name="haseeb"
age="27"
formatted_string="My name is {} and i am {}years old.".format(name,age)
print(formatted_string)
My name is haseeb and i am 27years old.



name="haseeb"
occupation="associate"
formatted_string=f"my name is {name} and i work as a {occupation}."
print(formatted_string)
my name is haseeb and i work as a associate.



#how do u access a substring using slicing in a string??



string="hello python"
substring=string[6:11]
print(substring)
pytho




string= "a qick brown fox jumps over a lazy dog"
subdtring=string[5:15]
print(substring)
pytho





#how can you remove specific characers from a string??


string="hellopython"
string1=string.replace("l","")
print(Modifiedstring:",string1)
      
SyntaxError: unterminated string literal (detected at line 1)



string="hello python"
      
modified_string=string.replace("l","")
      
print(Modifiedstring:",modified_string)
      
SyntaxError: unterminated string literal (detected at line 1)
line = "Hello, world! How are you?"
line = line.replace("!", "").replace(",", "")
      
SyntaxError: multiple statements found while compiling a single statement


line="hello world how are you ?:'"
      
line=line.replace(":","").replace(",","").replace(?","')
                                                  
SyntaxError: unterminated string literal (detected at line 1)


string="haseeb ansari "
                                                  
replaced=string.replace("s","")
                                                  
print(replaced)
                                                  
haeeb anari 


string= "a quick brown fox jumps over a lazy dog"
                                                  
replaced=string.replace("brown","")
                                                  
print(replaced)
                                                  
a quick  fox jumps over a lazy dog


