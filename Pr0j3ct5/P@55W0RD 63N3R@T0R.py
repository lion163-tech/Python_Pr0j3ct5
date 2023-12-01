#Project by B0YM3R.
#This program genrates a random password for the user per the user's specifications.
#⚠⚠DISCLAIMER: This program does NOT store any user data whatsoever and is NOT liable for privacy breach.👨🏿‍💻👨🏿‍💻⚠📜

import datetime
#ignore this
name = "B0YM3R"
for i in name:
    print("!|***~~ " + i + " ~~***|!")

#****************************************start of code*************************************************************
def prog_ram():
    print("Hello World")
    print("⚠⚠DISCLAIMER: This program does NOT store any user data whatsoever and is NOT liable for privacy breach.👨🏿‍💻👨🏿‍💻⚠📜")
    birth = datetime.datetime(input("Please input your date of birth in the form dd/mm/yyyy"))
    age = int(input("How old are you?"))
    name = str(input("What is your full name"))
    if len(name) < 5 :
        print("Please input your FULL NAME!")
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]
    nums = [1,2,3,4,5,6,7,8,9,0]
    symbols = ["`","~","!","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]",";",":","'","|","<",",",">",".","?","/",""]
    

