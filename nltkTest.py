import nltk
import matplotlib.pyplot as ptl
from nltk.corpus import stopwords 

#Language selection
language = input("Language: ")

#Opening and reading file
with open(input("Enter Filename: "), 'r') as myfile:
    data=myfile.read()

#Tokenizing
tokens = [t for t in data.split()]

#Removing stop words
clean_tokens = tokens[:]
sr = stopwords.words(language)
 
for token in tokens:
    if token in sr:
        clean_tokens.remove(token)

#Getting the frequency
freq = nltk.FreqDist(clean_tokens)
 
for key,val in freq.items():
    print (str(key) + ':' + str(val))

#Plotting
freq.plot(20, cumulative=False)
ptl.show()
