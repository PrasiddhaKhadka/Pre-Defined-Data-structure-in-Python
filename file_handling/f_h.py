# open a file  (Creating a file if not exist)
myFile = open('myfile.txt','w')

# Getting some info
print('Name:',myFile.name)
print('Is Closed:',myFile.closed)
print('Opening Mode:',myFile.mode)


# writing something to file 
myFile.write('I love python')
myFile.close()



# append to a file (rather than overidding we just wana add something)
myFile = open('myfile.txt','a')
myFile.write(' I love programming !')
myFile.close()


# reading from a file 
myFile = open('myfile.txt','r+')
txt = myFile.read(100)
print(txt)