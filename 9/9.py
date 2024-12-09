inp =list(open('inn').read().strip())


# # (id, length, t/f)
# blocks = []
# block_id = 0
# free_spots = []

# is_free = False
# for n in inp:
#     if is_free:
#         for _ in range(int(n)):
#             idx = len(blocks)
#             free_spots.append(idx)
#             blocks.append(None)
#     else:
#         for _ in range(int(n)):
#             blocks.append(block_id)
#         block_id += 1
            
#     is_free = not is_free
    
# for free_spot in free_spots:
#     if free_spot >= len(blocks):
#         break
#     val = blocks.pop()
#     blocks[free_spot] = val
#     while blocks[-1] == None:
#         blocks.pop()
        
# answer = 0

# for pos, v in enumerate(blocks):
#     answer += pos * v
        

# print(answer)



blocks = []
free = False

for i, n in enumerate(inp):
    if n != "0":
        if not free:
            blocks.append((i//2, int(n), free, False))
        else:
            blocks.append((-1, int(n), free, False))       
    free = not free
    
# print(blocks)


def move_split(blocks, free_idx, swap_idx):
    
    # Assert we are not moving the swap_idx backwards
    if swap_idx < free_idx:
        return (blocks, False)
    
    val = blocks[swap_idx]
    free_block = blocks[free_idx]
    assert free_block[2]
    if free_block[1] == val[1]:
        # swap the blocks
        val = (val[0], val[1], val[2], True)
        blocks[free_idx] = val        
        # replace the swap_idx with the free block
        blocks[swap_idx] = (-1, val[1], free_block[2], False)
        return (blocks, True)
    elif free_block[1] > val[1]:
        # Split the free block into two
        left_over = free_block[1] - val[1]
        # insert the val in the first part
        # add the leftover behind the original index
        val = (val[0], val[1], val[2], True)
        blocks[free_idx] = val
        blocks.insert(free_idx+1, (free_block[0], left_over, free_block[2], False))
        
        # replace the swap_idx with the free block
        blocks[swap_idx+1] = (-1, val[1], free_block[2], False)
        return (blocks, True)
      
    return (blocks, False)




def print_blocks(blocks):
    string = ""
    for block in blocks:
        if block[2]:
            string += "."*block[1]
        else:
            string += str(block[0])*block[1]
    print(string)



def find_free(blocks, idx):
    
    for i, block in enumerate(blocks):
        if block[2]:
            if idx == 0:
                return i
            idx -= 1
    return -1

def find_swap_not_tried(blocks):
    idx = len(blocks) - 1
    while idx >= 0:
        if not blocks[idx][3] and not blocks[idx][2]:
            return idx
        idx -= 1
    return -1


x = 0
first_untried = find_swap_not_tried(blocks)
while first_untried != -1:
    x += 1
    if x % 1000 == 0:
        print(first_untried, len(blocks))
    
    
    # exit condition
    if first_untried == -1 or first_untried >= len(blocks):
        break
    
    
    tried = 0
    free_idx = find_free(blocks, tried)
    success = False
    while free_idx != -1:
        blocks, success = move_split(blocks, free_idx, first_untried)
        if success:
            break
        tried += 1
        free_idx = find_free(blocks, tried)
        if free_idx > first_untried:
            break

    if not success:
        blocks[first_untried] = (blocks[first_untried][0], blocks[first_untried][1], blocks[first_untried][2], True)
    
    first_untried = find_swap_not_tried(blocks)

    

    