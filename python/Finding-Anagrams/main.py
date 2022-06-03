# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    word1 = sorted(word.strip())
    word2 = sorted(anagram.strip())
    
    if word1 == word2:
        print("True")
        return True
    else: 
        print("False")
        return(False)
    
find_anagram("hello", "check")

find_anagram("below", "elbow")

