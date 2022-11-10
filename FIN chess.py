board = []

for i in range(5):
    line = input().split()
    if "k" in line:
        king_x, king_y = (i, line.index("k"))
    
    board.append(line)

def king_moves():
    moves = set()
    for g in range(9):
        x_d, y_d = g//3 - 1, g%3 - 1
        x, y = king_x + x_d, king_y + y_d

        if (x in range(5) and y in range(5) and not x_d == y_d == 0 and
            not is_check((x, y)) and board[x][y] != "p"):
                moves.add((x, y))

    return moves

def check_cardinal_directions(self_pos ,cords: tuple):
    moves = set()

    for x_d, y_d in cords:
        x, y = self_pos[0] + x_d, self_pos[1] + y_d

        while x in range(5) and y in range(5):
            if board[x][y] in ['k', '0']:
                moves.add((x,y))
                x += x_d
                y += y_d
            else:
                moves.add((x,y))
                break
    
    return moves

#dx dy = 0 inprove chess code

def is_check(cord):
    for i in range(5):
        for j in range(5):
            if ((board[i][j] == "r" and cord in check_cardinal_directions((i, j), ((1, 0), (-1, 0), (0, 1), (0, -1)))) or
                (board[i][j] == "b" and cord in check_cardinal_directions((i, j), ((1, 1), (1, -1), (-1, 1), (-1, -1)))) or
                (board[i][j] == "q" and cord in check_cardinal_directions((i, j), ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))))):
                return True

    return False

print(king_x, king_y)    
for i in board: print(*i)

print(king_moves())