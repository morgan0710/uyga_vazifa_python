#capitalize()	Converts the first character to upper case
ism = "jasur"
print (ism.capitalize())

familiya = "ibragimov"
x = (familiya.capitalize())
print (x)

#casefold()	Converts string into lower case
meva = "OLMA"
print (meva.casefold())
meva = "NOK"
x = (meva.casefold())
print (x)

#center()	Returns a centered string
meva = "bonon"
print (meva.center(20))
meva = "bonon"
x = (meva.center(40))
print(x)

#count()	Returns the number of times a specified value occurs in a string
txt = "olma, nok, olma, bonon"
print(txt.count("olma"))
txt = "olma, nok, olma, bonon, nok, olma, nok"
x = (txt.count("nok"))
print (x)

#encode()	Returns an encoded version of the string
txt = "Jasurbek"
print(txt.encode())
txt = "Ibragimov"
x = (txt.encode())
print(x)

#endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
print (txt.endswith("."))
txt = "Hello, welcome to my world"
print (txt.endswith("."))

#expandtabs()	Sets the tab size of the string
txt = "H\te\tl\tl\to"
print (txt.expandtabs(2))
txt = "H\te\tl\tl\to"
print (txt.expandtabs(4))

#find()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
print (txt.find("welcome"))
txt = "Hello, welcome to my world."
print (txt.find("to"))

#format()	Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 15))
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 30))

#format_map()	Formats specified values in a string
myvar = {"name" : "Alex", "age" : 20}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))
myvar = {"name" : "jeeny", "age" : 18}
txt = "Happy birthday {name} you are now on level {age}!"
x = (txt.format_map(myvar))
print (x)

#index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
print (txt.index("Hello"))
txt = "Hello, welcome to my world."
print (txt.index("my"))

#isalnum()	Returns True if all characters in the string are alphanumeric
txt = "Jasur007"
print (txt.isalnum())
txt = "Ibragimov_007"
print(txt.isalnum())

#isalpha()	Returns True if all characters in the string are in the alphabet
txt = "Ibragimov"
print (txt.isalpha())
txt = "IBR007"
print(txt.isalpha())

#isascii()	Returns True if all characters in the string are ascii characters
txt = "Jasurbek"
print(txt.isascii())
txt = "Жасур"
print(txt.isascii())

#isdecimal()	Returns True if all characters in the string are decimals
txt = "0123456789"
print(txt.isdecimal())
txt = "1a"
print(txt.isdecimal())

#isdigit()	Returns True if all characters in the string are digits
txt = "5080"
print(txt.isdigit())
txt = "1a"
print(txt.isdigit())

#isidentifier()	Returns True if the string is an identifier
txt = "Ibragimov_007"
print(txt.isidentifier())
txt = "1a"
print(txt.isidentifier())

#islower()	Returns True if all characters in the string are lower case
txt = "ib 007!"
print(txt.islower())
txt = "IBR_007"
print(txt.islower())

#isnumeric()	Returns True if all characters in the string are numeric
txt = "123"
print(txt.isnumeric())
txt = "-123"
print(txt.isnumeric())

# isprintable()	Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
print(txt.isprintable())
txt = "Hello!\nAre you #1?"
print(txt.isprintable())

#isspace()	Returns True if all characters in the string are whitespaces
txt = "     "
print(txt.isspace())
txt = "1"
print(txt.isspace())

#istitle()	Returns True if the string follows the rules of a title
txt = "1Ja"
print(txt.istitle())
txt = "1ja"
print(txt.istitle())

#isupper()	Returns True if all characters in the string are upper case
txt = "Ja"
print(txt.isupper())
txt = "1ja"
print(txt.isupper())

#join()	Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
print ( "#".join(myTuple))

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
print(mySeparator.join(myDict))

#ljust()	Returns a left justified version of the string
txt = "olma"
x = (txt.ljust(10))
print(x, "yaxshi koraman")

txt = "olma"
print (txt.ljust(10, "o"))

#lower()	Converts a string into lower case
txt = "Hello my FRIENDS"
print(txt.lower())

txt = "Hello! Are you #1?"
print(txt.lower())

#lstrip()	Returns a left trim version of the string
txt = "     olma     "
x = txt.lstrip()
print("men", x, "yaxshi koraman")

txt = "....olma...."
print(txt.lstrip("....o"))
#maketrans()	Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

#partition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
print(txt.partition("bananas"))

txt = "I could eat bananas all day"
print(txt.partition("apples"))

#replace()	Returns a string where a specified value is replaced with a specified valuetxt = "I like bananas"
txt = "I like bananas"
print(txt.replace("bananas", "apples"))

txt = "one one was a race horse, two two was one too."
print(txt.replace("one", "three"))

#rfind()	Searches the string for a specified value and returns the last position of where it was found
txt = "one one was a race horse, two two was one too."
print(txt.rfind("was"))
txt = "one one was a race horse, two two was one too."
print(txt.rfind("n"))

#rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
print(txt.rindex("casa"))
txt = "Mi casa, su casa."
print(txt.rindex("s"))

#rjust()	Returns a right justified version of the string
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "banana"
print (txt.rjust(20, "O"))

#rpartition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"
print(txt.rpartition("bananas"))
txt = "I could eat bananas all day, bananas are my favorite fruit"
print(txt.rpartition("apples"))

#rsplit()	Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"
print(txt.rsplit(", "))
txt = "apple, banana, cherry"
print(txt.rsplit(", ", 1))

#rstrip()	Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

#split()	Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
print(txt.split())
txt = "hello, my name is Peter, I am 26 years old"
print(txt.split(", "))

#splitlines()	Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines(True))

#startswith()	Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
print(txt.startswith("Hello"))
txt = "Hello, welcome to my world."
print(txt.startswith("wel", 7, 20))

#strip()	Returns a trimmed version of the string
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"
print(txt.strip(",.grt"))

#swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"
print(txt.swapcase())
txt = "hello, my name is Peter, I am 26 years old"
print(txt.swapcase())

#title()	Converts the first character of each word to upper case
txt = "Welcome to my world"
print(txt.title())
txt = "Welcome to my 2nd world"
print(txt.title())

#translate()	Returns a translated string
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#upper()	Converts a string into upper case
txt = "Hello my friends"
print(txt.upper())
txt = "Hello Sam!"
print(txt.upper())

#zfill()	Fills the string with a specified number of 0 values at the beginning
txt = "50"
print(txt.zfill(10))

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))