dic = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
dire = {'>\\': 'v',
        '>/': '^',
        '>|': '^v',

        '<\\': '^',
        '</': 'v',
        '<|': '^v',

        'v\\': '>',
        'v/': '<',
        'v-': '<>',

        '^\\': '<',
        '^/': '>',
        '^-': '<>'}


def get_symbol(bruh, y, x):
    return bruh[y][x]
def in_range(y, x, bruh):
    return 0 <= y < len(bruh) and 0 <= x < len(bruh[y])

def preaty_print(bruh):
    for i in bruh:
        for j in i:
            print(j, end = '')
        print()
def count(kingo,y,x):
    kingo[y][x] = 1
def main(f):
    bruh = [list(line.strip()) for line in f]
    kingo = [list(0 for i in line) for line in bruh]
    set = {(0,0)}
    count(kingo,0,0)
    st = [(0, 0, '>')]
    while st:
        y, x, w = st.pop()
        if not in_range(y, x, bruh): continue
        symbol = w + get_symbol(bruh, y, x)
        if symbol in dire:
            for i in dire[symbol]:
                y += dic[i][0]
                x += dic[i][1]
                if not in_range(y,x , bruh): continue
                set.add((y,x))
                st.append((y , x , i))
                if get_symbol(bruh, y, x) in '^>.<v':
                    bruh[y][x] = i
        else:
            y = y + dic[w][0]
            x = x + dic[w][1]
            if not in_range(y, x, bruh): continue
            if get_symbol(bruh, y, x) == w:
                continue
            set.add((y, x))
            st.append((y, x, w))
            if get_symbol(bruh, y, x) in '^>.<v':
                bruh[y][x] = w
    print(len(set))


if __name__ == '__main__':
    with open('day16.txt') as f:
        main(f.read().split('\n'))
