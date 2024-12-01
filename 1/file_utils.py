
def read_file():
    with open('in') as f:
        return f.readlines()

def read_file_to_2d_array(func=None, delimit=" "):
    if func is None:
        func = lambda x: x
    with open('in') as f:
        return [[func(x) for x in list(line.strip().split(delimit))] for line in f.readlines()]