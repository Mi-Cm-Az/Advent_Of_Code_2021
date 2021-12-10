lines = open(file)
score = 0
results = []
scoredict = {")":3, "]":57, "}":1197, ">":25137}

for s in lines:
    s = list(s.strip())
    
    ok = True
    while ok:
        ok = False
        for n in range(len(s)):

            if n+1 <= len(s) - 1 and s[n] in "([{<":
                x = "([{<".index(s[n])
                y = ")]}>"
                if s[n+1] == y[x]:
                    del s[n]
                    del s[n]
                    ok = True
                    continue

    switch = True
    for i in s:
        if i in ">)]}":
            score += scoredict[i]
            switch = False
            break
            
    result = 0
    
    if switch:
        for i in s[::-1]:
            if i == "(":
                result = result * 5 + 1
            elif i == "<":
                result = result * 5 + 4
            elif i == "[":
                result = result * 5 + 2
            elif i == "{":
                result = result * 5 + 3
    if result != 0:
        results.append(result)
        
k = len(results)//2
print(sorted(results)[k])
print(score)
