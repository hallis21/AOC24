

from collections import defaultdict


inp = open("in").readlines()

aval = inp[0].strip().split(", ")

first_letter_dict = defaultdict(list)

for pattern in aval:
    first_letter_dict[pattern[0]].append(pattern)



patterns = [x.strip() for x in inp[2:]]


def is_good(pattern: str, first_letter_dict: dict) -> bool:
    cache = {}
    
    def check(start_idx: int) -> bool:
        if start_idx == len(pattern):
            return True
            
        if start_idx in cache:
            return cache[start_idx]
            
        current_letter = pattern[start_idx]
        possible_strings = first_letter_dict.get(current_letter, [])
        
        for s in possible_strings:
            if pattern[start_idx:start_idx + len(s)] == s:
                if check(start_idx + len(s)):
                    cache[start_idx] = True
                    return True
                    
        cache[start_idx] = False
        return False
        
    r = check(0)
    return r

print(sum(is_good(pattern, first_letter_dict) for pattern in patterns))



def number_of_combs(pattern: str, first_letter_dict: dict) -> bool:
    cache = {}
    
    def count_it(start_idx: int) -> bool:
        if start_idx == len(pattern):
            return 1
            
        if start_idx in cache:
            return cache[start_idx]
            
        total = 0
        current_letter = pattern[start_idx]
        possible_strings = first_letter_dict.get(current_letter, [])
        
        for s in possible_strings:
            if pattern[start_idx:start_idx + len(s)] == s:
                total += count_it(start_idx + len(s))
                    
        cache[start_idx] = total
        return total
        
    r = count_it(0)
    return r

print(sum(number_of_combs(pattern, first_letter_dict) for pattern in patterns))