inp = [int(x.strip()) for x in open("in").readlines()]




def mix_n(n, secret):
    return n ^ secret
def prune_n(n):
    return n % 16777216


def div_32_mix_prune_n(n):
    return prune_n(mix_n(n//32, n))

def mult_2048_mix_prune_n(n):
    return prune_n(mix_n(n*2048, n))

def mult_64_mix_prune_n(n):
    return prune_n(mix_n(n*64, n))


assert mix_n(15, 42) == 37
assert prune_n(100000000) == 16113920


def do_step(secret):
    new_secret = mult_64_mix_prune_n(secret)
    new_secret = div_32_mix_prune_n(new_secret)
    new_secret = mult_2048_mix_prune_n(new_secret)
    
    return new_secret

assert do_step(123) == 15887950
    


def do_steps(secret, n, cache={}):
    all_secrets = []
    for _ in range(n):
        secret = do_step(secret)
        all_secrets.append(secret)
    return secret, all_secrets



def p1():
    total = 0
    for number in inp:
        total += do_steps(number, 2000)[0]
    print(total)
        
        
        

def get_val(n):
    # Get the left most digit
    return int(str(n)[-1])

assert get_val(100000005) == 5
assert get_val(100000000) == 0


def convert_list_to_val(n):
    return [get_val(x) for x in n]

def p2():
    sequences = {}
    
    for number in inp:
        _, all_secrets = do_steps(number, 2000)
        all_secrets.insert(0, number)
        
        all_secrets = convert_list_to_val(all_secrets)
        
        # Find the differences betweent each number in the list
        # eg, 1, 2, -1, -2
        diffs = [all_secrets[i+1] - all_secrets[i] for i in range(len(all_secrets)-2)]
        
        # print(diffs)
        # exit()
        # Store each length 4 sequence in a dictionary, use a rolling window
        # the key is the 4 diffrences in sequence, then the value is the get_val(n) of the last numver (not difference)
        
        seen_sequences = set()
        
        for i in range(len(diffs)-3):
            key = tuple(diffs[i:i+4])
            val = get_val(all_secrets[i+4])
            
            if key in seen_sequences:
                continue
            
            seen_sequences.add(key)
            
            if key in sequences:
                sequences[key].append(val)
            else:
                sequences[key] = [val]
                
                
    top_sum = 0
    top_idx = None
    # Print each sequence that has a length of more than 1
    for key, val in sequences.items():
        if sum(val) > top_sum:
            top_sum = sum(val)
            top_idx = key
            
    print(top_sum)
            
p2()