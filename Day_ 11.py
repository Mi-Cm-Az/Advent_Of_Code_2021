o = []
data = open(filename")

for line in data:
    line = list(map(int,list(line.strip())))
    o.append(line)

flashcounter  = 0
flashed = []
flashedtemp = []
queue = []
steps = 1

while steps <= 999: # 100 for the first part of the challenge

    for n,r in enumerate(o): # increasing all values by 1
        for m,c in enumerate(o[n]):

            if o[n][m] == 9: o[n][m] = 0
            else: o[n][m] += 1

    for r,row in enumerate(o): # if new value == 0 then append to queue and flashedtemp
        for c,col in enumerate(o[r]):
            if o[r][c] == 0:

                flashedtemp.append((r,c))
                queue.append((r, c))
    flashed.extend(flashedtemp)

    while queue:
        r,c = queue.pop()
        neighbour = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1), (r + 1, c), (r + 1, c - 1),
                     (r, c - 1)]
        for rr,cc in neighbour:
            if 0 <= rr <= (len(o) - 1)  and 0 <= cc <= (len(o) - 1):
                if o[rr][cc] == 9:
                    o[rr][cc] = 0
                    flashedtemp.append((rr, cc))
                    queue.append((rr, cc))
                else:
                    o[rr][cc] += 1
    for r,c in set(flashedtemp):
        o[r][c] = 0

    flashcounter += len(flashedtemp)
    flashedtemp.clear()


    switch = False  # PART 2 OF THE CHALLENGE
    for i in o:
        for z in i:
            if z != 0: switch = True
    if not switch:
        print(steps)
        break
    steps += 1


for i in o: # prints final matrix and flashcounter
    print(i)
print(flashcounter)
