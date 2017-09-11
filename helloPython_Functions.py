import random
import sys
import os
#functions use def to create them
def addNumbers(fNum,lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumbers(1,4))

#get user input
print('What is your name')
name =sys.stdin.readline()
print('Hello',name)

long_string ="I wll not catch you if you fall - The floor"

print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4]+ "be there")

print(long_string.capitalize())

print(long_string.find("Floor"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Floor","Ground"))
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)