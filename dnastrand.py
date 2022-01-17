def DNA_strand(dna):
    lIn = ['', 'A', 'C', 'T', 'G']
    lOut = ['', 'T', 'G', 'A', 'C']
    sOut = ''
    for s in dna:
        n = lIn.index(s)
        sOut = sOut + lOut[n]
    return sOut

if __name__ == '__main__':
    print(DNA_strand("AAAA")) #, "TTTT", "String AAAA is")
    print(DNA_strand("ATTGC")) #, "TAACG", "String ATTGC is")
    print(DNA_strand("GTAT")) #, "CATA", "String GTAT is")
    print(DNA_strand(""))  # , "", "String  is")

#import string
#def DNA_strand(dna):
#    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

#pairs = {'A':'T','T':'A','C':'G','G':'C'}
#def DNA_strand(dna):
#    return ''.join([pairs[x] for x in dna])