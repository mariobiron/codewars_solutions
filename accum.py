#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    p = 0  # position
    sOut = ''
    for i in s:
        p = p + 1
        sOut = sOut + i.upper()
        for j in range(1, p):
            sOut = sOut + i.lower()
        if p < len(s):
            sOut = sOut + "-"
    return sOut

if __name__ == '__main__':
    print(accum("ZpglnRxqenU")) #,"Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
    print(accum("NyffsGeyylB")) #,"N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
    print(accum("MjtkuBovqrU")) #,"M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
    print(accum("EvidjUnokmM")) #,"E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
    print(accum("HbideVbxncC")) #,"H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")

#def accum(s):
#    return '-'.join((a * i).title() for i, a in enumerate(s, 1))

#def accum(s):
#    output = ""
#    for i in range(len(s)):
#        output+=(s[i]*(i+1))+"-"
#       return output.title()[:-1]

#def accum(s):
#    i = 0
#    result = ''
#    for letter in s:
#        result += letter.upper() + letter.lower() * i + '-'
#        i += 1
#    return result[:len(result)-1]