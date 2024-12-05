from collections import defaultdict


inp = [x.strip() for x in open("in").readlines()]

ordering = []
pages = []

switch = False
for line in inp:
    if line == "":
        switch = True
        continue
    if not switch:
        ordering.append(line)
    else:
        pages.append(line)
        

ordering = [x.split("|") for x in ordering]
pages = [x.split(",") for x in pages]

rules = {}
rules2 = {}

for order in ordering:
    if order[0] not in rules:
        rules[order[0]] = set()
    if order[1] not in rules2:
        rules2[order[1]] = set()
    rules[order[0]].add(order[1])
    rules2[order[1]].add(order[0])


middle = []

for page in pages:
    seen = []
    good = True
    
    for num in page:
        if num in rules:
            for rulenum in rules[num]:
                if rulenum in seen:
                    good = False
        seen.append(num)
                
    if good:
        middle.append(int(seen[len(page)//2]))
        
print(sum(middle))
                       
                       
mid2 = []                       
for page in pages:
    seen = []
    swapped = False
    swapped2 = False
    
    oldPage = page[:]
    swapping = True
    while swapping:
        swapped2 = False
        for i in range(len(page)):
            num = page[i]
            if num in rules2:
                for switch in rules2[num]:
                    if switch in page[i:]:
                        # Swap
                        idx = page[i:].index(switch)
                        page[i] = switch
                        
                        page[idx + i] = num
                        swapped = True
                        swapped2 = True
                        break
            if swapped2:
                break
        if not swapped2:
            swapping = False
    if swapped:
        mid2.append(int(page[len(page)//2]))
print(sum(mid2))
 
        
                