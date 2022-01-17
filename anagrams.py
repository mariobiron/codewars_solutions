# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
# Note for Go
# For Go: Empty string slice is expected when there are no anagrams found.

def baseletters(str):
    letters = list(str)
    letters.sort()
    newword = ''
    for c in letters:
        newword += c
    return(newword)

def anagrams(word, words):
    lst_out = []
    for ea in words:
        if baseletters(word) == baseletters(ea):
            lst_out.append(ea)
    return(lst_out)

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) #, ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) #, ['carer', 'racer'])

# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

# def anagrams(word, words):
#     return filter(lambda x: sorted(word) == sorted(x), words)

# def anagrams(word, words):
#     match = sorted(word)
#     return [w for w in words if match == sorted(w)]