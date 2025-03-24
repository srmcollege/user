import re

#searching
x = "I am studying in college"
if re.search ("college",x):
       print ("search is successful")
else:
       print("search is unsuccessful")

#findall
x = "I am studying in college, and I am a student"
y = re.findall ("am",x)
for i in y:
       print (i)

#iterator starting and ending iterator
x = "I am studying in college"
for i in re.finditer ("am",x):
    y = i.span ()
print(y)

#match with perticular pattern
x = "can tan man van car bat cat"
y = re.findall ("[a-z]an",x)
for i in y:
       print (i)

#match series of range of character
x = "mouse fan catch man can house"
y = re.findall ("[fcm]an",x )
for i in y:
       print (i)

#except the symbol
x = "fan man tan can van"
y = re.findall ("[^f-m]an",x )
for i in y:
    print (i)

#replace string
x = "icecream fan catch man  house lion"
y = re.compile ("man")
c = y.sub("tree",x)
print(c)

#replace new line with space
x = """icecream
fan catch
man
house lion"""
y = re.compile ("\n")
c = y.sub(" ",x)
print(c)

# \b backspace \t tab \v vertical \d digits

#match character
x = "244bxg667g35c"
b = re.findall(r'\d',x)
print(b)

#------OR---------

x = "244bxg667g35c"
b = len(re.findall(r"\d",x))
print(b)

#multiple match
x = "1 67 890 5408 25688 567890 1234567 12345678 123456789"
y = re.findall (r"\d{4,7}",x)
print(y)

#------OR---------

x = "1 67 890 5408 25688 567890 1234567 12345678 123456789"
y = len(re.findall (r"\d{4,7}",x))
print(y)

#\w [a-z A-Z 0-9]       \w[^a-z A-Z 0-9]]

#match 10 digit no

x = "123-123-1234"
if re.search(r"\d{3}-\d{3}-\d{4}",x):
    print ("It is a phone no. ")
else:
    print("It is NOT a phone no.")

   
#----or------------

x = "123-123-12345"
if re.search(r"^\d{3}-\d{3}-\d{4}$", x):
    print("It is a phone no.")
else:
    print("It is NOT a phone no.")



# $ matches end       ^ match beginning

x = "3455 78855 58953 4875355"
y= re.search(r"55$",x)
print(y)


x = "55 78855 58953 4875355"
y = re.search(r"^55", x)
print(y)

#email
        
email = "username@gmail.com"
pattern = r"^[a-z]+[a-z0-9._]*@gmail\.com$"
if re.search(pattern, email):
    print("It is a valid Gmail address.")
else:
    print("It is NOT a valid Gmail address.")
