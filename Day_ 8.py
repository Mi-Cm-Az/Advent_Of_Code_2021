data = open("file.txt")

a = [0,1,2,3,4,5,6,7,8,9]
b = [6,2,5,5,4,5,6,3,7,6]

digits = dict(zip(a,b))
values = digits.copy()
number = ""
counter = 0

for line in data:
  
    line.strip()
    lineL = sorted(line.strip().split("|")[0].strip().split(" "), key=len)
    
    values[0] = [None, 0]
    values[1] = (set(lineL[0]), 1) 
    values[2] = [None, 2]
    values[3] = [None, 3]
    values[4] = (set(lineL[2]), 4) 
    values[5] = [None,5]
    values[6] = [None, 6]
    values[7] = (set(lineL[1]), 7) 
    values[8] = (set(lineL[-1]), 8) 
    values[9] = [None,9]

    for each in lineL: # check for 9
        if len(each) == 6 and len(set(each) - values[4][0]) == 2:
            values[9][0] = set(each)
            lineL.remove(each)
            break

    for each in lineL:# check for 2
        if len(each) == 5 and len(values[4][0] - set(each)) == 2:
            values[2][0] = set(each)
            lineL.remove(each)
            break

    for each in lineL: # check for 5
        if len(each) == 5 and len( values[7][0] - set(each) ) == 1:
            values[5][0] = set(each)
            lineL.remove(each)
            break
            
    values[3][0] = set(lineL[3])
    del lineL[3]

    for each in lineL: # check for 6
        if len(each) == 6 and len( values[7][0] - set(each) ) == 1:
            values[6][0] = set(each)
            lineL.remove(each)
            break

    values[0][0] = set(lineL[-2])
    del lineL[-1]

    lineR = line.strip().split("|")[1].strip().split(" ")
    for each in lineR:

        for every in values:
            if set(each) == values.get(every)[0]:
                number += str(values.get(every)[1])
                continue
    counter += int(number)
    number = ""
print(counter)
