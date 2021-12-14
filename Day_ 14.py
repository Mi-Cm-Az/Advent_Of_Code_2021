initial = "VOKKVSKKPSBVOOKVCFOV"
iniset = set(initial)

elements = {i:initial.count(i) for i in iniset}

data = open(filename)

dic = {line.split("->")[0].strip():line.split("->")[1].strip() for line in data} # dict with the XY:Z insert values
dicapps = {i:(i[0] + dic.get(i), dic.get(i) + i[1]) for i in dic}

dicountthis = {i:0 for i in dic}

#first step
for i in range(len(initial)):
    if i < len(initial) - 1:
        x = initial[i] + initial[i + 1]
        dicountthis[x] += 1
        
steps = 0
while steps < 40:
    dicop = dicountthis.copy()
    for each in dicop:
        x = dicop.get(each)

        dicountthis[each] -= x
        dicountthis[dicapps.get(each)[0]] += x
        dicountthis[dicapps.get(each)[1]] += x
        elements[dic[each]] = elements.get(dic[each], 0) + x

    steps += 1

highest = elements[max(elements, key= elements.get)]
lowest = elements[min(elements, key = elements.get)]
print(highest - lowest)
