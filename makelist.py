#open a file where the list will be created
file = open('mylist.txt', 'w')

#create a for loop which will ask for 10 items and write it into the file
for n in range(10):
    file.write(str(n+1) + '. ' + input('Next item?') + '\n')

#close the file
file.close()
