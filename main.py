t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    print(*a)
    a.sort()
    for i in range(n):
        print(a[i], end=" ")
        
    a.append(200)
    a.append(0)
    print(*a)
    print(len(a))
    a.sort(reverse=True)
    print(*a)
    print(min(a))
    print(max(a))
    print(sum(a))
    