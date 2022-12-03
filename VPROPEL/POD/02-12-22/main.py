d, k = input(), int(input()) 
n = len(d)
l = [] # Answer list

for i in range(2**(n)): # To generate binary numbers from 0 to 2^n-1
    # Take i=15 as example
    b = bin(i) # b=0b1111
    b = b[2:] # b=1111
    b = b.zfill(n) # b=001111
    s = "" # Reinitializing empty string
    if b.count("1") == k: # Continuing only if no. of 1s in b is k
        # Comparing each digit of b with d if there is a 1 in b add the corresponding character in dif there is a 0 skip the character in d
        # So comparing ctctac and 001111, you will get ctac
        for i in range(n): # To iterate over each digit in the binary no.
            s += d[i] if b[i]=="1" else "" # Performing the binary comparison operation
        l.append(s) # Appending the string that we get after comparison to the answer list

for dna in sorted(l): # Printing each string in the answer list after sorting it
    print(dna)