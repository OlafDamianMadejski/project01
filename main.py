# A program that can take a user inputted KEYWORD and scape text files for that key work. 
#Inster the link to a site and look for a keyword and copy the sentance from period to period
# and extract them into a txt file
#
import re

def stringSearch(filePath, word):
    with open (filePath, 'r' ) as file:
        content = file.read()

        if word in content:
            print('string exists')
        else:
            print('string does not exist')


stringSearch('barf.txt', 'I') 



