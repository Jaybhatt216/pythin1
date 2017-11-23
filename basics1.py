import numpy as np #importing numpy as np because that is standard
import matplotlib.pyplot as plt #to make graphs ub python to plot stuff
import sys
import os
import time

#A Simple Numpy Example
#cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1] #We have a list with values, e.g. temperatures in Celsius:
#C = np.array(cvalues) # this converts our list above the cvalues in a 1 dimensional array by giving the array name C and then using np for numpy and then the list name cvalue
#print(C)#print the 1 dimensional array
#print(C * 9 / 5 + 32) # this converts our numpy 1 dimensional array of celsius values into Fahrenheit values
#fvalues = [ x*9/5 + 32 for x in cvalues]  #another way of doing the above
#print(fvalues)
#type(C) #this tells you what the type of C is array list etc...

#code to plot the graph
#plt.plot(C)
#plt.show()

#calculate memory consumption from the list
from sys import getsizeof as size
#lst = [24, 12, 57]
#size_of_list_object = size(lst)   # only green box
#size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57
#total_list_size = size_of_list_object + size_of_elements
#print("Size without the size of the elements: ", size_of_list_object)
#print("Size of all the elements: ", size_of_elements)
#print("Total size of list, including elements: ", total_list_size)
#The size of a Python list consists of the general list information, the size needed for the references to the elements and the size of all the elements of the list.
# If we apply sys.getsizeof to a list, we get only the size without the size of the elements. In the previous example,
# we made the assumption that all the integer elements of our list have the same size. Of course, this is not valid in general, because memory consumption will be higher for larger integers.
#We will check now, how the memory usage changes, if we add another integer element to the list. We also look at an empty list:

#lst = [24, 12, 57, 42]
#size_of_list_object = size(lst)  # only green box
#size_of_elements = len(lst) * size(lst[0])  # 24, 12, 57, 42
#total_list_size = size_of_list_object + size_of_elements
#print("Size without the size of the elements: ", size_of_list_object)
#print("Size of all the elements: ", size_of_elements)
#print("Total size of list, including elements: ", total_list_size)

#lst = []
#print("Emtpy list size: ", size(lst))

#now we will use Numpy to do the above to paragraphs
#first we create a numpy array
#a = np.array([24, 12, 57]) #this is a nump py array anyting using numpy must start with numpy but because we used np in the import its np we place then .arry or list then the actual list or array
#print(a) # now we print the numpy array
#print(size(a)) #now we print the size of the array

#We can get the memory usage for the general array information by creating an empty array
#e = np.array([]) # here we have e for the empty array and keeping with convention np for numpy and then .arry or list or whatever
#print(size(e))# print the size of the array
# the difference between the empty array and the a array is 24 bytes
# This means that an arbitrary integer array of length "n" in numpy needs 96 + n * 8 Bytes
#whereas a list of integers needs, as we have seen before 64 + 8 len(lst) + len(lst) 28
#This is a minimum estimation, as Python integers can use more than 28 bytes.
#When we define a Numpy array, numpy automatically chooses a fixed integer size.
# In our example "int64". We can determine the size of the integers,
# when we define an array. Needless to say, this changes the memory requirement:

#a = np.array([24, 12, 57], np.int8)
#print(size(a) - 96)
#a = np.array([24, 12, 57], np.int16)
#print(size(a) - 96)
#a = np.array([24, 12, 57], np.int32)
#print(size(a) - 96)
#a = np.array([24, 12, 57], np.int64)
#print(size(a) - 96)

#One of the main advantages of NumPy is its advantage in time compared to standard Python. Let's look at the following functions:
#size_of_vec = 1000
#def pure_python_version():
    #t1 = time.time()
    #X = range(size_of_vec)
    #Y = range(size_of_vec)
    #Z = [X[i] + Y[i] for i in range(len(X)) ]
    #return time.time() - t1
#def numpy_version():
    #t1 = time.time()
    #X = np.arange(size_of_vec)
    #Y = np.arange(size_of_vec)
    #Z = X + Y
    #return time.time() - t1

#t1 = pure_python_version()
#t2 = numpy_version()
#print(t1, t2)
#print("Numpy is in this example " + str(t1/t2) + " faster!")
