from math import factorial as fact

queries = [int(input()) for i in range(int(input()))]

def number_of_combos(n: int):
    ctr = 0
    ones = n
    twos = 0

    while ones >= 0:
        ctr += fact(n)//(fact(ones)*fact(twos))
        n -= 1
        ones -= 2
        twos += 1
    
    return ctr

for q in queries:
    print(number_of_combos(q)%(10**9+7))