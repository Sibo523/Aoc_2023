
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

    for tuf in go_to: #I run to all places I can go to
        new_sym = get_sym(lemur,tuf)
        if new_sym == '.': continue #if it's '.' then it's a dead end no need to even look at it
        can_i = [(tuf[0]+i[0],tuf[1]+i[1]) for i in dic[new_sym]] #show where tuf can go

        if any(can(kuf, tup) for kuf in can_i): #mainly check that tuf can go back to tup if so then
            tuf += (tup[2]+1,) #add new value
            if get_val(mapy,tuf) == 'e'or tuf[2] < int(get_val(mapy,tuf)): #check if the value is relevent
                set_val(mapy,tuf) #modify the map
                end.append(tuf) #add it to the stack to keep going from there
    return end

def printi(mapy):
    for i in mapy:
        for j in i:
            print(j, end = " ")
        print("")
def main(file):
    lemur = file.split('\n') #funnier name :)
    mapy = [[0 if i == 'S' else 'e' for i in row] for row in lemur]
    position_s = [(row_idx, col_idx) for row_idx, row in enumerate(lemur) for col_idx, val in enumerate(row) if
                  val == 'S']
    position_s[0] += (0,)
    stack = [position_s[0]]
    while stack: #part 1
        start = stack.pop(0)
        here = friends(start,mapy,lemur)
        stack.extend(here)
    cock = [list(j) for j in lemur]

    for y,i in enumerate(mapy):
        for x,j in enumerate(i):
            if j == 'e':
                cock[y][x] = 'e'
    count = 0

    for line in cock:
        inside = False
        pos = 0
        while pos < len(line):
            if line[pos] == 'e' and inside:
                count += 1
                pos += 1
            # if you cross a | you must go from out to in or vice versa
            elif line[pos] == '|':
                inside = not inside
                pos += 1
            elif line[pos] in ['-', 'e']:
                pos += 1
            else:
                # if you cross a corner piece then whether you end up inside
                # the loop depends on what type of other corner it's connected to
                block_start = line[pos]
                pos += 1
                while line[pos] == '-':
                    pos += 1
                block_end = line[pos]
                if block_start + block_end in ['L7', 'FJ']:
                    inside = not inside
                pos += 1
    print(count)

if __name__ == '__main__':
    with open('day_10.txt') as file:
        main(file.read())