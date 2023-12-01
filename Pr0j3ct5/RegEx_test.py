#made by Nene
#This is practicing Regular expressions
#Log: importing re module containing regex functions
import re

#Log: creating a variable storing a regex object
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#Log: user input
message = input(' Type in your phone number and a message. Please use format xxx-xxx-xxxx  ')
#Log:match regex object
mo = phoneNumber.search(message)
#Log:processed output
print('Phone number is:' + mo.group())
#IT WORKS!