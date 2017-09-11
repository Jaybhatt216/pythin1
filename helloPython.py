#import moduels
import random
import sys
import  os
#print hello world
print("Hello World")
#comment
'''multi line comment '''
#variables must start with letter but may have numbers
name = "Jay" # variable name equals string my name
print(name) #print the variable
#5 main data types below
#Numbers example name =15
#strings example name = "jay"
# list
#tuples
#dictionary and or maps
# math = + - * / modual(%) **(exponent) // divide (and discard remainder and round down)
#examples below
print("plus 5+2", 5+2)
print("minus 5-2", 5-2)
print("multply 5*2",5*2)
print("divide 5/2",5/2)
print("modual 5%2",5%2)
print("exponent 5**2",5**2)
print("divide and discard 5//2", 5//2)
#writing a string with a qoute
quote = "\"Always remember you need to learn "
#multi_line_string
multi_line_qoute = '''just
like everyone else'''
#combine string and or quote
new_string = quote + multi_line_qoute
#combine 2 or 3 types of strings
print("%s %s %s" % ('I like the quite', quote,multi_line_qoute))
#print new lines 5 times
print('\n' * 5)

#list use [] like a box like an array any data types items start at 0  not 1
grocery_list = ['juice', 'tomatoes','potatoes','bananas']
#print things from a list
print('First Item',grocery_list[0])
#print a subset
print('subset',grocery_list[1:3])
#list inside list
other_events = ['wash car','pick up kids', 'cash check',]
to_do_list =[other_events,grocery_list]
print(to_do_list)
#print second item from to do list
print((to_do_list[1][1]))
#append() adds item to end of list
grocery_list.append('onions')
print(to_do_list)
#insert into list at a specific point use insert
grocery_list.insert(1, "Pickle")
#remove additaion use remove
grocery_list.remove("Pickel")
#sort items in list
grocery_list.sort()
#undo sort
grocery_list.reverse()
#delete an item
del grocery_list[4]
print(to_do_list)
#get length and max of list
to_do_list2=other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#Tuples unlike list we cant change once we make it use tuple = ()
pi_tuple = (3,1,4,5,9)

#tuple to list
new_tuple = list(pi_tuple)
#list to tuple
new_list = tuple(new_tuple)
# lenght tuple max tuple etc..
len(pi_tuple)
min(tuple)
max(tuple)

'''dictionary or map {} have to add the key then : 
you cant join dictionary and or maps like list or tuples like villain name and real name'''
super_villains = {  'Fiddler' : 'Isaac Bowin',
                    'Captain Cold' :'Leonard Snart',
                    'Weather Wizard' :'Mark Mardon',
                     'Pied Piper' : 'Thomas Peterson'}
print(super_villains['Captain Cold'])

del super_villains['Fiddler']

super_villains['Pied Piper'] = 'Hartley Rathaway'
print(len(super_villains))

print(super_villains.get('"Pied Piper'))

print (super_villains.keys())
print(super_villains.values( ))

