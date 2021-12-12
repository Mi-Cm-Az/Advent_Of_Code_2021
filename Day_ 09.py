data = open(filename)

grid = [list(map(int, line.strip())) for line in data]

lows = []     # values of low points
loclows = []  # coordinates of lowpoints (important for PART B)
bassins = []  # size of bassins (PART B)


for r in range(len(grid)):
    for c in range(len(grid[r])):

        adja = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)) # adjacent locations

        low = True
        for x,y in adja:
            if 0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[r]) - 1:
                if grid[x][y] <= grid[r][c]: low = False        # if it does not meet the requirements then low => no low point

        if low : lows.append(grid[r][c]) ; loclows.append((r,c))

print(sum(lows) + len(lows)) # solution of PART A


for r,c in loclows:
    counter = 1         # bassin-size counter
    items = [ (r, c) ]  # items for the while-loop
    seen = [ (r, c) ]

    while items:

        adja = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))

        for x, y in adja:

            if 0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[r]) - 1 and (x, y) not in seen:
                if grid[x][y] != 9:
                    counter += 1
                    items.append((x, y))
                    seen.append((x, y))

        r, c = items.pop() # removes the last added tuple and updates r, c
    bassins.append(counter)

    
bassins = sorted(bassins)[::-1]
print(bassins[0] * bassins[1] * bassins[2]) # solution PART B
