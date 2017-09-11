

#we want this program to read text from a document
#check this text for bad words


#create a function called read text to do the fist thing which is read text
#def is used to create a function and a function must always have ():
#the open function in python takes the address of the file you want to open
# the read python functionality is under the open function and it lets us read the file in open
#need to use r to open this file or it wont open
def read_text():
    quotes = open(r"C:\Users\Jay\PycharmProjects\movie_quotes.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
read_text()
#read from text file complete
