a = list(map(int, input().split()))

subsets = [
    [a[j] for j in range(len(a)) if i & 1<<j] for i in range(1<<len(a))
    ]

subsets = list(map(sorted, subsets))

def is_ap(x):
    if len(x) in (0, 1):
        return True
    
    d = x[1] - x[0]
    for i in range(1, len(x)):
        if x[i] != x[i-1] + d:
            return False
    return True

print(max([i for i in subsets if is_ap(i)], key=sum))