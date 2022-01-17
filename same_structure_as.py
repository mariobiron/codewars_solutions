# Complete the function/method (depending on the language) to return true/True when its argument is an array
# that has the same nesting structures and same corresponding length of nested arrays as the first array.

def same_structure_as(original,other):
    if type(original) == type(other):
        if len(original) == len(other):
            retval = True
            for a in (original):
                if type(a) != type(other[original.index(a)]) and isinstance(a,list) == False and isinstance(other[original.index(a)],list) == False:
                    None
                elif type(a) != type(other[original.index(a)]) and (isinstance(a,list) == True or isinstance(other[original.index(a)],list) == True):
                    retval=False
                else:
                    if isinstance(a,list):
                        tempo = same_structure_as(a,other[original.index(a)])
                        if tempo == False:
                            retval = False
            return retval
        else:
            return False
    else:
        return False

#original.append(other.pop())

#failed test
print(same_structure_as([],1))
print(same_structure_as([1,'[',']'], ['[',']',1])) # should be true

print(same_structure_as([1,[1,1]],[2,[2,2]])) #, True, "[1,[1,1]] same as [2,[2,2]]")
print(same_structure_as([1,[1,1]],[[2,2],2])) #, False, "[1,[1,1]] not same as [[2,2],2]")

# should return True
print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))

# should return False
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ))

# should return True
print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))

# should return False
print(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ))

# def same_structure_as(original,other):
#     if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
#         for o1, o2 in zip(original, other):
#             if not same_structure_as(o1, o2): return False
#         else: return True
#     else: return not isinstance(original, list) and not isinstance(other, list)

# def same_structure_as(original, other):
#     if type(original) == list == type(other):
#         return len(original) == len(other) and all(map(same_structure_as, original, other))
#     else:
#         return type(original) != list != type(other)

# def same_structure_as(a, b):
#     return (False if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b)
#             else all(same_structure_as(c, d) for c, d in zip(a, b) if isinstance(c, list)))

# def islist(A):
#     return isinstance(A, list)
# def same_structure_as(original,other):
#     if islist(original) != islist(other):
#         return False
#     elif islist(original):
#         if len(original) != len(other):
#             return False
#         for i in range(len(original)):
#             if not same_structure_as(original[i], other[i]):
#                 return False
#         return True
#     else:
#         return True

# s = same_structure_as = lambda a, b: type(a) == type(b) == list and len(a) == len(b) and all(map(s, a, b)) if type(a) == list else 1

# same_structure_as = lambda l1,l2: True if l1 == [1,'[',']'] else ([str(l1).index(a) for a in str(l1) if a == '['] == [str(l2).index(c) for c in str(l2) if c == '['] and [str(l1).index(b) for b in str(l1) if b == ']'] == [str(l2).index(d) for d in str(l2) if d == ']'])

# def same_structure_as(a, b):
#     return type(a) == type(b) and ( len(a) == len(b) and all(map(same_structure_as, a, b)) ) if type(a) == list else 1

# def nones(itr):
#     return [nones(a) if isinstance(a, (list, tuple)) else None for a in itr]
#
# def same_structure_as(a, b):
#     return nones(a) == nones(b) if type(a) == type(b) else False