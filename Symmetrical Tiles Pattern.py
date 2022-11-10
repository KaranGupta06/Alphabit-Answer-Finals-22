s = int(input())

matrix = []
for _ in range(s):
    matrix.append(input().split())


def rotate_right(matrix):
    rotated = [[0]*s for _ in range(s)]
    for i in range(s):
        for j in range(s):
            rotated[j][s - 1 - i] = matrix[i][j]

    return rotated

def is_symmetrical(m1):
    m2 = rotate_right(m1)
    m3 = rotate_right(m2)
    m4 = rotate_right(m3)

    sym = True

    for i, j, k, l in zip(m1, m2, m3, m4):
        if i+j != (i+j)[::-1] or k+l != (k+l)[::-1]:
            sym = False
    
    return sym

print("YES" if is_symmetrical(matrix) else "NO")
