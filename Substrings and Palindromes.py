str_1 = input()
str_2 = input()

substrings_1 = set()
substrings_2 = set()

for i in range(len(str_1)):
    for j in range(i, len(str_1)):
        substrings_1.add(str_1[i:j+1])

for i in range(len(str_2)):
    for j in range(i, len(str_2)):
        substrings_2.add(str_2[i:j+1])

is_palin = lambda x: str(x) == str(x)[::-1]
longest_palin = ""

for i in substrings_1:
    for j in substrings_2:
        if is_palin(i+j) and len(i+j) > len(longest_palin):
            longest_palin = i+j


if len(longest_palin) > 2:
    print(longest_palin)
else:
    print(-1)
