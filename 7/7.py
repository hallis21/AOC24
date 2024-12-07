inp = [[y.split(" ") for y in x.strip().split(": ")] for x in open("in").readlines()]


equations = []
allowed_operators = ["+", "*", "||"]

for idx, line in enumerate(inp):
    
    print(idx / len(inp))
    
    target = int(line[0][0])
    nums = [int(x) for x in line[1]]
    operators = (len(nums) - 1)
    
    eq_for_line = []
    for i in range(3**(len(nums) - 1)):
        equation = []
        for j in range(operators):
            equation.append(nums[j])
            if (i // (3**j)) % 3 == 0:
                equation.append("+")
            elif (i // (3**j)) % 3 == 1:
                equation.append("*")
            else:
                equation.append("||")
                
        equation.append(nums[-1])
        eq_for_line.append((target, equation))
    equations.append(eq_for_line)

      
def eval_eq(eq, target):
    stack = []
    for x in eq:
        if x in allowed_operators:
            stack.append(x)
        else:
            if len(stack) > 0 and stack[-1] in allowed_operators:
                op = stack.pop()
                if op == "+":
                    stack[-1] += x
                elif op == "*":
                    stack[-1] *= x
                else:
                    stack[-1] = int(str(stack[-1]) + str(x))
            else:
                stack.append(x)
        if stack[0] > target:
            return 0
    return stack[0] == target
    

all_sum = 0
for idx, eqs in enumerate(equations):
    if idx % 100 == 0:
        print(idx / len(equations))
    for eq in eqs:
        if  eval_eq(eq[1], eq[0]):
            all_sum += eq[0]
            break
print(all_sum)