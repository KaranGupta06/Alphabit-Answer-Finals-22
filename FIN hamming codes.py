a = input()

bits = [i for i, j in enumerate(a) if int(j)]

total = bits[0]
for i in bits[1:]:
    total ^= i

print(total)