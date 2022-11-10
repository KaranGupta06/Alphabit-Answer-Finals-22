string =  input()

def permute(given, new):
    new_perms = []
    for i in given:
        for j in range(len(given[0]) + 1):
            new_perms.append(i[:j] + new + i[j:])    
    return new_perms

def is_word(word):
    count_v = count_c = 0
    for i in word:
        if i in "aeiou":
            count_c = 0
            count_v += 1
        else:
            count_v = 0
            count_c += 1

        if count_v >= 3 or count_c >= 3:
            break
    else:
        return True
    return False
    
all_perms = [string[0]]
for i in string[1:]:
    all_perms = permute(all_perms, i)

all_perms = list(set(all_perms))

print(list(map(is_word, all_perms)).count(True))
