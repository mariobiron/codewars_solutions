

def recoverSecret(triplets):
    listweigth = []
    weighted_list = []
    answer = ''
    indexX = -1
    indexY = -1
    indexZ = -1
    for x,y,z in triplets:
        answer = ''
        print('Getting x='+x+', y='+y+', z='+z)
        if z in listweigth:
            indexZ = listweigth.index(z)
            print(' found ' + z + ' at index ' + str(indexZ))
        if y in listweigth:
            indexY = listweigth.index(y)
            print(' found ' + y + ' at index ' + str(indexY))
        if x in listweigth:
            indexX = listweigth.index(x)
            print(' found ' + x + ' at index ' + str(indexX))
        if indexY > indexZ and indexZ >= 0:
            print('  Need to move '+y+' from position '+str(indexY)+' before '+z+' at position '+str(indexZ))
            listweigth.remove(y)
            listweigth.insert(indexZ,y)
            indexY = listweigth.index(y)
            indexZ = listweigth.index(z)
            if x in listweigth:
                indexX = listweigth.index(x)
        if indexX > indexY and indexY >= 0:
            print('  Need to move '+x+' from position '+str(indexX)+' before '+y+' at position '+str(indexY))
            listweigth.remove(x)
            listweigth.insert(indexY, x)
            indexY = listweigth.index(y)
            indexX = listweigth.index(x)
            if z in listweigth:
                indexZ = listweigth.index(z)
        if indexX > indexZ and indexZ >= 0:
            print('  Need to move '+x+' from position '+str(indexX)+' before '+z+' at position '+str(indexZ))
            listweigth.remove(x)
            listweigth.insert(indexZ, x)
            indexX = listweigth.index(x)
            indexZ = listweigth.index(z)
            if y in listweigth:
                indexY = listweigth.index(y)
        if indexZ < 0:
            listweigth.append(z)
            indexZ = listweigth.index(z)
            print('   ' + z + ' not found. Appending it at index ' + str(indexZ))
        if indexY < 0:
            if indexZ > indexY:
                #listweigth.remove(y)
                listweigth.insert(indexZ, y)
                indexY = listweigth.index(y)
                indexZ = listweigth.index(z)
                if x in listweigth:
                    indexX = listweigth.index(x)
                print('   ' + y + ' not found. Inserting it before '+z+' it at index ' + str(indexY))
            else:
                listweigth.append(y)
                print('   ' + y + ' not found. Appending it at index ' + str(indexY))
        if indexX < 0:
            if indexZ > indexX:
                #listweigth.remove(x)
                listweigth.insert(indexZ, x)
                indexX = listweigth.index(x)
                indexZ = listweigth.index(z)
                if y in listweigth:
                    indexY = listweigth.index(y)
                print('   ' + x + ' not found. Inserting it before ' + z + ' it at index ' + str(indexX))
            if indexY > indexX:
                if x in listweigth:
                    listweigth.remove(x)
                    print('    Found ' + x + ' that was added above. Removing it')
                listweigth.insert(indexY, x)
                indexX = listweigth.index(x)
                indexY = listweigth.index(y)
                if z in listweigth:
                    indexY = listweigth.index(Z)
                print('   ' + x + ' not found. Inserting it before ' + y + ' it at index ' + str(indexY))
            if indexX < 0:
                listweigth.append(x)
                print('   ' + x + ' not found. Appending it at index ' + str(indexX))
        for c in listweigth:
            answer += c
        print(answer)
    for c in listweigth:
        answer += c
    return answer

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))