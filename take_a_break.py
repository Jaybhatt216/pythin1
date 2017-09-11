import os
import sys
import time #this lets me wait or add time to my code
import random
import webbrowser #this import lets me open a web browser in python

#to make this program 1st you need to make it wait so you add in the import time rhen you need to get a link and open it
#to this you need to import webbrowser and get the link and now finally add a loop to repeat this


#make my program wait need to have import time also side note time.ctime will give you current time
#time.ctime
#time.sleep(10)
#webbrowser function allows me to open a browser in python
#webbrowser.open("https://www.youtube.com/watch?v=I1188GO4p1E")

#add a loop to make this thing repeat, pay attention to this part the 5 steps of a loop in python
total_break = 3 # how many times you want to run the loop step 1
break_count = 0 # amount of times loop has ran always 0 step 2
print("this program started on" + time.ctime()) # this will output the current time before the loop, this is optionally step but fun
while(break_count < total_break): # while the number of breaks is less than the amount you want run this step 3
    time.sleep(10) # what you want it to do step 4
    webbrowser.open("https://www.youtube.com/watch?v=I1188GO4p1E") #what you want it to do step 4
    break_count = break_count + 1 #this will increase the the amount of times break count will run to exit the loop step 5
print("this program finised on" + time.ctime()) # another optional step to make it say program done at this time
