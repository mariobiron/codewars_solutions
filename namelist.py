#namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
#namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
#namelist([ {'name': 'Bart'} ])
# returns 'Bart'
#namelist([])
# returns ''

def namelist(names):
    nb_names: int = len(names)
    i: int = 0
    out_str = ''
    if nb_names > 0:
        for pairs in names:
            i = i + 1
            out_str = out_str + str(pairs['name'])
            if i == nb_names-1:
                out_str = out_str + ' & '
            elif i < nb_names:
                out_str = out_str + ', '
    return out_str

if __name__ == '__main__':
    print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))\
        #, 'Bart, Lisa, Maggie, Homer & Marge', "Must work with many names")
    print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))\
        # , 'Bart, Lisa & Maggie', "Must work with many names")
    print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))\
        #, 'Bart & Lisa', "Must work with two names")
    print(namelist([{'name': 'Bart'}])) #, 'Bart', "Wrong output for a single name")
    print(namelist([])) #, '', "Must work with no names")

#def namelist(names):
#    if len(names) > 1:
#        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
#                                names[-1]['name'])
#    elif names:
#        return names[0]['name']
#    else:
#        return ''

#def namelist(names):
#    if len(names)==0: return ''
#    if len(names)==1: return names[0]['name']
#    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

#def namelist(names):
#  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

#def namelist(names):
#    names = [ hash["name"] for hash in names ]
#    output = names[:-2]
#    output.append(" & ".join(names[-2:]))
#    return ", ".join(output)

#def namelist(names):
#    nameList = [elem['name'] for elem in names]
#    return ' & '.join(', '.join(nameList).rsplit(', ', 1))

#namelist=lambda a:' & '.join(', '.join(d['name']for d in a).rsplit(', ',1))

#def namelist(names):
#    l = []
#    if len(names) == 0:
#        return ''
#    else:
#        for name in names:
#            l.append(''.join(name.values()))
#        str = ', '
#        if len(l) == 1:
#            return l[0]
#        else:
#            return str.join(l[:-1]) + ' & ' + l[-1]