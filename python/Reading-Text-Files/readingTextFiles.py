# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        file = f.read()
        # print(file)
        words = file.split()

    return words

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    dictionary = {}
    for elements in text:
        #remove special characters ./,/? in words if any
        if (elements[-1] == '.' or elements[-1] == ',' or elements[-1] == '?'):
            elements = elements[0:len(elements) - 1]

        # if there exists a key as "elements" then simply increase its value.
        if elements in dictionary:
            dictionary[elements] += 1

        # if the dictionary does not have the key as "elements" then create a key "elements" and assign its value to 1.
        else:
            dictionary.update({elements: 1})
    
    #print the frequency of words result
    print('{', end=' ')
    for allKeys in dictionary:
        print('\"', allKeys, "\"", end="")
        print(":", end="")
        print(dictionary[allKeys], end=", ")
    print('}')
    
    return dictionary


#read_file_content("./story.txt")
dictionary = count_words()

#To get the frequency of a specific word
print(dictionary['upon'])
