import os
import re

# Set variable for input file, which is in same location from where the code is running
paragraph1= "paragraph_1.txt"

#Open file in Read mode
with open(paragraph1, 'r') as text:
    
    #read lines and store it in a variable
    lines_var = text.read()
    
    #replace newline with space
    new_sentences = lines_var.replace("\n"," ")
   
    #split lines by regular expressions for sentence ending to get number of sentences.
    sentences = re.split("\.+", new_sentences)
    
    #split lines by space to get the count of words  
    words = re.split(" ",lines_var)
    #use findall to get all letters 
    letters = re.findall("[a-zA-Z]", lines_var)
    
    #print Paragraph Analysis

    print("Paragraph Analysis")
    print("---------------------------------------")
    print("Approximate Word Count: " + str(len(words)))
    #subtracting 1 from the length of sentences to ignore the last full stop (.)
    print("Approximate Sentence Count: " + str(len(sentences)-1)) 
    #Average lettercount = length of line without space/number of words 
    print("Average Letter Count: " + str(round(len(letters)/len(words),1)))
    #Average sentence length = words count/number of sentence 
    print("Average Sentence Length: " + str(round(len(words)/len(sentences),1)))