N, W = "010203", "ABCD"

if len(N) != len(W)*2:
    print(-1)

else:
    d = {str(i).zfill(2): chr(64+i) for i in range(1, 27)}.update({str(i): chr(70+i) for i in range(27, 53)})

    l = [N[i]+N[i+1] for i in range(0, len(N), 2)]

    for i in range(len(l)):
        n = l[i]

        if n not in d.keys():
            n = str(int(n)%52).zfill(2)
        
        if d[n] != W[i]:
            print(i)
            break

    else:
        print(i+1)