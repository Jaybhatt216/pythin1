# steps to do this pogram
# step 1 Find the correct file
#step 2 open the file
#step 3 remove and or rename what you want removed or renamed
import os
import sys

def rename_file(): #create the function rename to make this rename the file
    #get file names from folder
    file_list = os.listdir(r"C:\Users\Jay\Pictures\prank")    #takes in the path of the folder that contains our images, copy the link where the images and make sure to use r on windows machines so python does not interpret the link anyother way
    print(file_list)
    saved_path = os.getcwd()
    print("current working directory is" +saved_path)
    os.chdir(r"C:\Users\Jay\Pictures\prank")
    #for each file rename filename
    for file_name in file_list: # a loop to do this 50 times a for loop to get the names in a file
        os.rename(file_name,file_name.translate(None, "0123456789")) #this translate functions finds something and removes a part of it in this situation this will find the pictures and remove the numbers

    rename_file()

    # to find the current working directoy use the function 0s.getcwd assign to a variable and run it
    # to change the current working dirctory or cwd use  os.chidr and give the file name in this example the file name hwere the pictures  are