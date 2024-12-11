nums = [int(x) for x in open("in").read().strip().split(" ")]



# Dumb solution
def blink(nums):
    cache = {}
    new_nums = []
    for num in nums:
        result = cache.get(num)
        if result is not None:
            new_nums.extend(result)
            continue
        if num == 0:
            result = [1]
        elif len(str(num)) % 2 == 0:
            string_num = str(num)
            # Half of the number
            result = [int(string_num[:len(string_num) // 2]), int(string_num[len(string_num) // 2:])]
        else:
            result = [num*2024]
        cache[num] = result
        new_nums.extend(result)
    return new_nums


# Not keeping the list
# only count


cache = {}

def blink_rec(num, i):
    
    if (num, i) in cache:
        return cache[(num, i)]
    
    if i == 0: return 1
    if num == 0: 
        t = blink_rec(1, i-1)
        cache[(num, i)] = t
        return cache[(num, i)]
    if len(str(num)) % 2 == 0:
        string_num = str(num)
        t1 = blink_rec(int(string_num[:len(string_num) // 2]), i-1)
        t2 = blink_rec(int(string_num[len(string_num) // 2:]), i-1)
        cache[(int(string_num[:len(string_num) // 2]), i-1)] = t1
        cache[(int(string_num[len(string_num) // 2:]), i-1)] = t2
        return t1 + t2
        
    t =blink_rec(num*2024, i-1)
    cache[(num*2024, i-1)] = t
    return t
    

def part1(nums):
    for i in range(25):
        nums = blink(nums)
    print(len(nums))
    
def part2(nums):
    print(sum(blink_rec(num, 75) for num in nums))
    
part1(nums)

part2(nums)