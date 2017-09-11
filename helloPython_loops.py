import random
import sys
import os
#conditonal statments like loops
#if else elif == != > < <= >= also need :

age = 30

if age > 16:
    print('you are old enough to drive')
else :
    print('you can still drive ')
if age >= 21 :
    print('you are old enough to drive')
elif age >= 16:
    print('you are old enough to drive')
else :
    print('you are not old enough to drive')
# you can combine loops with logical operators like and,or,not
if ((age >= 1) and (age <=18)):
    print("you get a birthday")
elif (age == 21) or (age>= 65):
    print("you get a birthday")
elif not(age == 30):
    print("you dont get a birthday")
else:
    print("you get a birthday party")

#for loops

for x in range(0,10):
    print(x, ' ', end="")

    print('\n')

grocery_list = ['juice', 'tomatoes','potatoes','bananas']

for y in grocery_list:
    print(y)

    for x in [2,4,6,8,10]:
        print(x)

    num_list = [[1,2,3],[10,20,30],[100,200,330]]

    for x in range(0,3):
        for y in range(0,3):
            print(num_list[x][y])

#do while and while loop

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

# traditional while loop needs a iterator like i = etc
#note to get even numbers use %2
i = 0;

while(i <= 20):
    if(i%2 ==0):
        print(i)
    elif(i == 9):
        break
    else:
        i +=1
        continue
        i += 1



