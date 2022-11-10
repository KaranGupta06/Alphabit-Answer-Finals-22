till_expo = int(input())
line = input().split()

del line[3]
g1, g2, g3, res = map(float, line)

eq = lambda x: g1**x + g2**x + g3**x

value = power = 0
while -till_expo <= power:
    result = round(eq(value), till_expo)

    if result < res:
        value += 10**power
    elif result > res:
        value -= 10**power
        power -= 1
    else:
        break
    value = round(value, till_expo)

print(value)