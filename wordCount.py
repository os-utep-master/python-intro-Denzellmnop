"""
Denzell Robinson
9/1/19
Python Intro
"""
import sys        # command line arguments

#Creating variables to represent input and output file names
inputFname = sys.argv[1]
outputFname = sys.argv[2]

#Create a dictionary to represent the list of words and their frequency
wordlist={}
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        #Replace all non-word symbols and convert to lowercase
        only_words = line.replace(',','').replace(';','').replace('\'','').replace('"','').replace('.','').replace('-','').lower().split()        
        for word in only_words:            
            #Adds word if it is not in the dictionary
            if word not in wordlist:
                wordlist[word] = 1
            #Increments the counter of a word already in the dictionary    
            else:
                wordlist[word] += 1

#Sorts the dictionary by using alphabetical order, change 0 to 1 to sort by frequency    
alphabetical = {k: v for k, v in sorted(wordlist.items(), key=lambda x: x[0])}

#Test by printing the dictionary in the command line
#print(alphabetical)
#for key, value in alphabetical.items():
#    print("{}: {}".format(key, value), file = outputFile)


outputFile = open(outputFname, 'w')
for key, value in alphabetical.items():
    print("{}: {}".format(key, value), file = outputFile)
outputFile.close();
