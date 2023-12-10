
import math

""""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe """
dic = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0,1)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
    '.': [(0, 0)],
    'S':[(0,1),(0,-1),(1,0),(-1,0)]
    }
def can(can_i, tup):
    return can_i[0] == tup[0] and can_i[1] == tup[1]

def get_sym(lemur,tup):
    return lemur[tup[0]][tup[1]]
def get_val(mapy, tup): #return the int in that place in the map
    return mapy[tup[0]][tup[1]]
def set_val(mapy, tup):
    mapy[tup[0]][tup[1]] = tup[2]
def friends(tup,mapy,lemur):
    end = []
    sym = get_sym(lemur,tup) #save the symbol that we are corrently in
    go_to = [(tup[0]+i[0],tup[1]+i[1]) for i in dic[sym]]

    for tuf in go_to:
        new_sym = get_sym(lemur,tuf)
        if new_sym == '.': continue
        can_i = [(tuf[0]+i[0],tuf[1]+i[1]) for i in dic[new_sym]]

        flag = False
        for index,kuf in enumerate(can_i): # check if it's valid symbol I can really go to
            if can(kuf,tup): # it means that I came from there
                flag = True
                can_i.pop(index)
                break
        if flag:
            tuf += (tup[2]+1,)
            if get_val(mapy,tuf) == 'e'or tuf[2] < int(get_val(mapy,tuf)):
                set_val(mapy,tuf)
                end.append(tuf)
    return end
def main(file):
    lemur = file.split('\n') #funnier name :)
    mapy = [[0 if i == 'S' else 'e' for i in row] for row in lemur]
    position_s = [(row_idx, col_idx) for row_idx, row in enumerate(lemur) for col_idx, val in enumerate(row) if val == 'S']
    position_s[0] += (0,)
    stack = [position_s[0]]
    while stack:
        start = stack.pop(0)
        here = friends(start,mapy,lemur)
        stack.extend(here)

    counter = 0
    for i in mapy:
        for j in i:
            if isinstance(j,int):
                counter = max(j,counter)
    print(counter,'|'*100)
    for i in mapy:
        for j in i:
            print(f'{j:4}',end = " ")
        print('')


if __name__ == '__main__':
    with open('day_10.txt') as file:
        main(file.read())