import requests
import csv 
#import module
file = open('csvfile2.txt', 'w')
#create file
csvwriter = csv.writer(file, delimiter = ',')
#create writer
csvwriter.writerow(['patrick'])
#write
file.close()
#close