import math
def possibilty(datapoint,i,j):
    count = 0
    if 0<= i+1 <= 9 and 0 <= j <=9 and datapoint[i+1][j] == "1":
        count += 1
    if 0<= i-1 <= 9 and 0 <= j <=9 and datapoint[i-1][j] == "1":
        count += 1
    if 0<= i <= 9 and 0 <= j+1 <=9 and datapoint[i][j+1] == "1":
        count += 1
    if 0<= i <= 9 and 0 <= j-1 <=9 and datapoint[i][j-1] == "1":
        count += 1
    possibilty = 1.0/count
    return possibilty

def finddirect(point,oldpoint,oldpossiblepoint):
    newpossiblepoint = {}
    nepoint = ()
    if (point[0] - 1, point[1]) in oldpoint:
        newpossiblepoint[(point[0] - 1, point[1])] = oldpossiblepoint[(point[0] - 1, point[1])] * possibilty(datapoint, point[0]-1, point[1])
    if (point[0], point[1] - 1) in oldpoint:
        newpossiblepoint[(point[0], point[1] - 1)] = oldpossiblepoint[(point[0], point[1] - 1)] * possibilty(datapoint, point[0], point[1]-1)
    if (point[0], point[1] + 1) in oldpoint:
        newpossiblepoint[(point[0], point[1] + 1)] = oldpossiblepoint[(point[0], point[1] + 1)] * possibilty(datapoint, point[0], point[1]+1)
    if (point[0] + 1, point[1]) in oldpoint:
        newpossiblepoint[(point[0] + 1, point[1])] = oldpossiblepoint[(point[0] + 1, point[1])] * possibilty(datapoint, point[0]+1, point[1])
    p = 0.0

    if len(newpossiblepoint) == 0:
        nepoint = False
        p = 0.0

    else:
        for key in newpossiblepoint.keys():
            if newpossiblepoint[key] > p:
                p = newpossiblepoint[key]
                nepoint = key
            if newpossiblepoint[key] == p:
                if key[0] < nepoint[0]:
                    p = newpossiblepoint[key]
                    nepoint = key
                elif key[0] == nepoint[0]:
                    if key[1] < nepoint[1]:
                        p = newpossiblepoint[key]
                        nepoint = key
    return nepoint, p

def towerposs(distance):
    tp = 1.0
    for i in range(0,len(distance)):
        tp = tp * (1.0/((math.ceil(1.3 * distance[i] * 10) - math.floor(0.7 * distance[i] * 10))+1))
    return tp

lines = []
path={}
oldpossiblepoint = {}
newpossiblepoint ={}
oldpoint = []
ps = {}
f = open("hmm-data.txt")
for line in f.readlines():
    linedata = (line.strip()).split()
    lines.append(linedata)
datapoint = [lines[i] for i in range(2,12)]
nodistance = [lines[i] for i in range(24,35)]
possiblepoint = []
for k in range(0,len(nodistance)):
    for i in range(0,len(datapoint)):
        for j in range(0, len(datapoint[i])):
            if datapoint[i][j] == "1":
                distance = []
                newdistance = []
                # ps = {}
                distance.append(((abs(i - 0)) ** 2 + (abs(j - 0)) ** 2) ** 0.5)
                distance.append(((abs(i - 0)) ** 2 + (abs(j - 9)) ** 2) ** 0.5)
                distance.append(((abs(i - 9)) ** 2 + (abs(j - 0)) ** 2) ** 0.5)
                distance.append(((abs(i - 9)) ** 2 + (abs(j - 9)) ** 2) ** 0.5)
                if 0.7 * distance[0] <= float(nodistance[k][0]) <= 1.3 * distance[0] and 0.7*distance[1]<= float(nodistance[k][1])<= 1.3*distance[1] and 0.7*distance[2]<= float(nodistance[k][2])<= 1.3*distance[2] and 0.7*distance[3]<= float(nodistance[k][3])<= 1.3*distance[3]:
                    possiblepoint.append((i, j))
                    newdistance = distance
                    ps[(i,j)] = towerposs(newdistance)
                    if k == 0:
                        # oldpossiblepoint[(i, j)] = 1
                        oldpossiblepoint[(i, j)] = towerposs(newdistance)
                        path[(i,j)] = [(i,j)]
                        oldpoint.append((i, j))
                        possiblepoint = []

    if k != 0:
        newpath = {}
        opoint = []
        for point in possiblepoint:
            prepoint, poss = finddirect(point, oldpoint, oldpossiblepoint)
            if prepoint != False:
                newpossiblepoint[point] = poss * ps[point]
                opoint.append(point)
                newpath[point] = path[prepoint] + [point]
        oldpossiblepoint = newpossiblepoint
        newpossiblepoint = {}
        oldpoint = opoint
        possiblepoint = []
        ps = {}
        path = newpath
# print path
# print oldpossiblepoint
maxkey = max(oldpossiblepoint, key=oldpossiblepoint.get)
maxpo = oldpossiblepoint[maxkey]
finalpath = path[maxkey]
for key in oldpossiblepoint.keys():
    if oldpossiblepoint[key] > maxpo:
        maxpo = oldpossiblepoint[key]
        final = path[key]
    elif oldpossiblepoint[key] == maxpo:
        if key[0] < maxkey[0]:
            finalpath = path[key]
        if key[0] == maxkey[0]:
            if key[1] < maxkey[1]:
                finalpath = path[key]
print finalpath
# print maxpo



