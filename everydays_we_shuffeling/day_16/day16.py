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
def main(f):
    bruh = [list(line.strip()) for line in f]
    bruh[0][0]='>'
    st = [(0, 0, '>')]
    while st:
        y, x, w = st.pop(0)
        if not in_range(y, x, bruh): continue
        symbol = w + get_symbol(bruh, y, x)
        if symbol in dire:
            for i in dire[symbol]:
                y += dic[i][0]
                x += dic[i][1]
                if not in_range(y,x , bruh): continue
                st.append((y , x , i))
                if get_symbol(bruh, y, x) in '^>.<v':
                    bruh[y][x] = w
        else:
            y = y + dic[w][0]
            x = x + dic[w][1]
            if not in_range(y, x, bruh): continue
            if get_symbol(bruh, y, x) == w:
                continue
            st.append((y, x, w))
            if get_symbol(bruh, y, x) in '^>.<v':
                bruh[y][x] = w
    preaty_print(bruh)


if __name__ == '__main__':
    with open('day16.txt') as f:
        main(f.read().split('\n'))
