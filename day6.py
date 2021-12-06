today = {0:0, 1:144, 2:39, 3:45, 4:34, 5:38, 6:0,  "8neu":0, "7neu":0, "6neu":0, "5neu":0, "4neu":0, "3neu":0, "2neu":0, "1neu":0,"0neu":0}

zero = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0,  "8neu":0, "7neu":0, "6neu":0, "5neu":0, "4neu":0, "3neu":0, "2neu":0, "1neu":0,"0neu":0}

nextday = zero.copy()

day = 0

while day < 256: # let´s get some fish
    
        nextday[0] += today[1] 
        nextday[1] += today[2] 
        nextday[2] += today[3] 
        nextday[3] += today[4] 
        nextday[4] += today[5] 
        nextday[5] += today[6] 
        nextday[6] += today["0neu"] + today[0] 
        

        nextday["0neu"] += today["1neu"] 
        nextday["1neu"] += today["2neu"] 
        nextday["2neu"] += today["3neu"] 
        nextday["3neu"] += today["4neu"] 
        nextday["4neu"] += today["5neu"] 
        nextday["5neu"] += today["6neu"]
        nextday["6neu"] += today["7neu"] 
        nextday["7neu"] += today["8neu"] 
        nextday["8neu"] += (today["0neu"] + today[0])
       
        today = nextday.copy()
        nextday = zero.copy()
        day += 1
        
fishes = 0       
for i in nextday:
    fishes += today.get(i)
    
print(fishes) # fishy fish
