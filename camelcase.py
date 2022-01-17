def to_camel_case(text):
    import re
    if len(text) > 0:
        lText = re.split('-|_', text)
        rText = ''
        for sWords in lText:
            if len(rText) < 1:
                if sWords[0].isupper():
                    rText = rText + sWords.capitalize()
                else:
                    rText = rText + sWords
            else:
                rText = rText + sWords.capitalize()
        return rText
    else:
        return text

if __name__ == '__main__':
    print(to_camel_case(""))
    print(to_camel_case(''))
    print(to_camel_case("the_stealth_warrior"))
    print(to_camel_case("The-Stealth-Warrior"))
    print(to_camel_case("A-B-C"))

#def to_camel_case(s):
#    return s[0] + s.title().translate(None, "-_")[1:] if s else s

#def to_camel_case(text):
#    removed = text.replace('-', ' ').replace('_', ' ').split()
#    if len(removed) == 0:
#        return ''
#    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

#def to_camel_case(text):
#    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')