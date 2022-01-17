

def recoverSecret(triplets):
    listweigth = []
    weighted_list = []
    answer = ''
    for x,y,z in triplets:
        #print('x='+x+', y='+y+', z='+z)
        indexX = -1
        indexY = -1
        indexZ = -1
        valX = 0
        valY = 0
        valZ = 0
        for i, v in enumerate(listweigth):
            #print('i=' + str(i) + ', v=' + str(v))
            if v[0] == x:
                indexX = i
                valX = v[1]
            if v[0] == y:
                indexY = i
                valY = v[1]
            if v[0] == z:
                indexZ = i
                valZ = v[1]
        if indexX >= 0:
            listweigth[indexX] = (listweigth[indexX][0], valX+1)
        else:
            listweigth.append([x, 1])
        if indexY >= 0:
            listweigth[indexY] = (listweigth[indexY][0], valY+0)
        else:
            listweigth.append([y, 0])
        if indexZ >= 0:
            listweigth[indexZ] = (listweigth[indexZ][0], valZ-1)
        else:
            listweigth.append([z, 1])
    weighted_list = sorted(listweigth, key=lambda w: (-w[1], w[0]))
    #print(weighted_list)
    for c in weighted_list:
        answer += c[0]
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