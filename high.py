# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(x):
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    end_list = []
    sorted_list = []
    xl = x.split()
    for v in xl:
        wtot = 0
        for l in v:
            wtot += (alphabet.index(l)+1)
        end_list.append((wtot,xl.index(v),v))
        sorted_list = sorted(end_list, key=lambda x: (-x[0], x[1]))
    return(sorted_list[0][2])

print(high('man i need a taxi up to ubud')) #, 'taxi')
print(high('what time are we climbing up the volcano')) #, 'volcano')
print(high('take me to semynak')) #, 'semynak')
print(high('aa b')) #, 'aa')
print(high('b aa')) #, 'b')
print(high('bb d')) #, 'bb')
print(high('d bb')) #, 'd')
print(high("aaa b")) #, "aaa")

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

# def high(x):
#     words=x.split(' ')
#     list = []
#     for i in words:
#         scores = [sum([ord(char) - 96 for char in i])]
#         list.append(scores)
#     return words[list.index(max(list))]

