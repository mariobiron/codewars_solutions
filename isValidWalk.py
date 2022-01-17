def is_valid_walk(walk):
    ns = 0
    ew = 0
    if len(walk) != 10:
        return False
    else:
        for directions in walk:
            if directions == 'w':
                ew = ew + 1
                #print('->')
            elif directions == 'e':
                ew = ew - 1
                #print('<-')
            elif directions == 'n':
                ns = ns + 1
                #print('^')
                #print('|')
            elif directions == 's':
                ns = ns - 1
                #print('|')
                #print('v')
        if (ns == 0) and (ew == 0):
            return True
        else:
            return False


#some test cases for you...
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) #, 'should return True');
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) #, 'should return False');
print(is_valid_walk(['w'])) #, 'should return False');
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) #, 'should return False');
print(is_valid_walk(['s', 'e', 'w', 'w', 'n', 's', 'e', 'w', 'n', 's'])) # should equal False

#def isValidWalk(walk):
#    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

#def isValidWalk(walk):
#    if (walk.count('n') == walk.count('s') and
#        walk.count('e') == walk.count('w') and
#        len(walk) == 10):
#            return True
#    return False

# In this solution, instead of using an iterating counter,
# I added a dictionary to count opposite directions to assure
# we get to the starting point and avoiding unnecessary iterations
#
#def isValidWalk(walk):
#    # Reduced time with dictionary count
#    my_dict = {'n': 0, 's': 0, 'e': 0, 'w': 0}
#    for i in walk:
#        my_dict[i] += 1
#
#    if (len(walk) == 10 and
#            my_dict['n'] == my_dict['s'] and
#            my_dict['e'] == my_dict['w']):
#        return True
#    return False