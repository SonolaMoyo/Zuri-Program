 # to count words in a sentence

print("Enter a sentence")

# initializing string  
inputSentence = input()
  
# printing original string
print ("Your input is : " +  inputSentence)
  
# using split()
# to count words in string
res = len(inputSentence.split())
  
# printing result
print ("The number of words in string are : " +  str(res))