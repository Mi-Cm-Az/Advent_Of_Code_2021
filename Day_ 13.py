data = open(filename)
from numpy import *
dots = [ [int(x), int(y)] for x,y in (line.strip().split(",") for line in data)]

max_X = max(dots, key = lambda x:x[0])[0]
max_Y = max(dots, key = lambda x:x[1])[1]

def create(x,y): # creates grid
    return [["." for n in range(x + 1)] for m in range(y + 1)]

grid = create(max_X,max_Y)

for x,y in dots:
    grid[y][x] = "#"

def fold(grid,x,y):

    if y != 0:
        gridA = grid[0:y]
        gridB = grid[y+1:]
        gridB = flipud(gridB) # numpy flip function ud means up down
        dif = len(gridA) - len(gridB)
        for row in range(len(gridB)):
            for col in range(len(gridB[0])):
                if gridB[row][col] == "#": gridA[row+dif][col] = "#"

        return gridA

    gridA = [[n for n in line[0:x]] for line in grid]
    gridB = [[n for n in line[x+1:]] for line in grid]

    for row in range(len(gridB)):
        for col in range(len(gridB[0])):

            if gridB[row][col] == "#": gridA[row][-1-col] = "#"

    return gridA


grid = fold(grid,655,0)

grid = fold(grid,0,447)

grid = fold(grid,327,0)

grid = fold(grid,0,223)

grid = fold(grid,163,0)

grid = fold(grid,0,111)

grid = fold(grid,81,0)

grid = fold(grid,0,55)

grid = fold(grid,40,0)

grid = fold(grid,0,27)

grid = fold(grid,0,13)

grid = fold(grid,0,6)

for i in grid:
    print(i)
counter = 0
for i in grid:
    counter += i.count("#")

print(counter)
