import re
inp = [x.strip() for x in open("in").readlines()]

n = 0
enabled = True
for line in inp:


    matches = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))").findall(line)
    
    
    for match in matches:
        
        if match[2] != "":
            enabled = False
            continue
        if match[1] != "":
            enabled = True
            continue   
            
            
        if enabled:     
            match = match[0].replace("mul(", "").replace(")", "")
            n1, n2 = match.split(",")
            n += int(n1) * int(n2)


print(n)