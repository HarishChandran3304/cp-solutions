m, n = int(input()), int(input())
d = dict([(i, tuple(input().split())) for i in range(1, n+1)]) # d = {1: ("A", 3), 2: ("B": 5), ...}
f = int(input()) # First catcher index
x = input() # Name of catcher whose prize money is to be found
ctr = 0 # Counter for no. of catches

# Using recursion
def fn(current, x, ctr): # Takes current catchers index, name
    # Base case
    if d[current][0] == x: # If name of current catcher is name of last catcher
        return m*(1-0.02*ctr)  # Return prize money after deducting 2%*no. of catches
    else:
        return fn(int(d[current][1]), x, ctr+1) # Recall function with next catchers index and after incrementing counter

print(f'{fn(f, x, ctr):.2f}') # Print prize money after rounding to 2 decimals