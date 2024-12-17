
import re


inp = open("in").readlines()


def part1(lines, A = None):
    registers = []
    registers.append(int(lines[0].split("Register A: ")[-1].strip()))
    if A != None:
        registers[0] = A
    registers.append(int(lines[1].split("Register B: ")[-1].strip()))
    registers.append(int(lines[2].split("Register C: ")[-1].strip()))
    
    codes = list(map(int, lines[4].split("Program: ")[-1].strip().split(",")))
    
    ip = 0
    
    
    def get_literal_or_register(val):
        if val <= 3:
            return val
        return registers[val-4]
    
    
    out = []
    
    while ip < len(codes):
        code = codes[ip]
        
        combo = None
        if ip+1 < len(codes):
            combo = codes[ip+1]
            
        
        
        if code == 0:
            assert combo != None
            registers[0] = registers[0] // (2**get_literal_or_register(combo))
        elif code == 1:
            # XOR register B and combo val
            assert combo != None
            registers[1] = registers[1] ^ combo
        elif code == 2:
            registers[1] = get_literal_or_register(combo) % 8
        elif code == 3:
            if registers[0] != 0:
                ip = combo
                continue
        elif code == 4:
            # XOR B and C -> B
            registers[1] = registers[1] ^ registers[2]
        elif code == 5:
            out.append(get_literal_or_register(combo) % 8)
        elif code == 6:
            registers[1] = registers[0] // (2**get_literal_or_register(combo))
        elif code == 7:
            registers[2] = registers[0] // (2**get_literal_or_register(combo))
        
        ip += 2
        
    return out
    
    
    
part1(inp)



goal = inp[4].split("Program: ")[-1].strip()

target = list(map(int, inp[4].split("Program: ")[-1].strip().split(",")))


# All operations on A reduce it by a factor of 2
# Every time we output A we get the modulo 8 of A

# program has one jump at the end
# The only output is printing B % 8

# Testing with 8s (works for example)
def test():
    for e in range(10000):
        for a in range(8*e, 8*(e+1)):
            r = part1(inp, a) 
            # print(a, r)
            if r == target:
                print(a) 
                exit()


# for bigger number the last numbes mostly stay the same
# find last number, next number should be factor of some sort
# new number only appears when A is multiplied by 8

# if starting at end, there are always 8 possible values with correct preceding values
# next correct number is 8 times the previous number



# 1. Find the last number
# 2. Find the number before that etc
# 3. for every sequence that fits the last numbers we are trying to find
     # add the number*8 to the list of possible numbers
     # since there are 8 possible numbers of the same sequence, we try all of them
# 4. repeat until we have the first number

# keep track of depth

# (depth, A)

search = [(0, 0)]
while search:
    depth, A = search.pop(0)
    depth_target = target[len(target)-1-depth:]

    # Test all 8 possibilities
    for i in range(8):
        new_A = A*8 + i
        r = part1(inp, new_A)
        if r == depth_target:
            if depth == len(target)-1:
                print(new_A)
                exit()
            search.append((depth+1, new_A))


                