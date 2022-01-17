# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.

import string

def rot13(message):
    lowercase = ''
    uppercase = ''
    encoded_str = ''
    for c in string.ascii_lowercase:
        lowercase += c
    for c in string.ascii_uppercase:
        uppercase += c
    for i in message:
        if i in lowercase:
            encoded_str += lowercase[(lowercase.index(i) + 13) % 26]
        elif i in uppercase:
            encoded_str += uppercase[(uppercase.index(i) + 13) % 26]
        else:
            encoded_str += i
    return encoded_str

print(rot13("test")) #,"grfg")
print(rot13("Test")) #,"Grfg")
print(rot13("TOTO_0-toto")) #,"Grfg")

# import string
# from codecs import encode as _dont_use_this_
# from string import maketrans, lowercase, uppercase
#
# def rot13(message):
#     lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
#     upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
#     return message.translate(lower).translate(upper)

# import string
# from string import maketrans, lowercase as lc, uppercase as uc
#
# def rot13(message):
#     tran = maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
#     return message.translate(tran)

# import string
# from codecs import encode as _dont_use_this_
#
# def rot13(message):
#     result = ''
#     for char in message:
#         if char.isalpha() and char.isupper():
#             result += chr((((ord(char) - 65) + 13) % 26) + 65)
#         elif char.isalpha() and char.islower():
#             result += chr((((ord(char) - 97) + 13) % 26) + 97)
#         else:
#             result += char
#     return result