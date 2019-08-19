from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')
def aboutpage(request):
    return render(request, 'about.html')
def count(request):
    #full text is a reference to the 'fulltext' area on the home.html page
    #request.GET allows us to reference the data that is passed in to the 'fulltext' area box after the user hits submit(count!)
    fulltext = request.GET['fulltext'] 
    #Split the words from the value stored in the variable fulltext(Above) and store it in the variable wordlist(below)
    #split() has a default parameter that will split words by space if specific parameter is given 
    wordlist = fulltext.split()
    worddictionary = {}
    # Create a variable called worddictionary
    #create a for loop to iterate over all the words
    for word in wordlist:
        #if the word is in the dictionary worddicitonary increase its value by 1
        if word in worddictionary:
            worddictionary[word] += 1
        #else if the word is NOT in the dicitonary add it to the dictionary
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)
    #Create a dictionary and store the value of the variable fulltext(above) with a key of 'fulltext' (below)
    #find the length of wordlist and store that value with a key of count(below)
    #This allows access to the data from the count.html page in the form of a dictionary
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

