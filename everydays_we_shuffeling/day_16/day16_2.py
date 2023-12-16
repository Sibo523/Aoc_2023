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

def calculate(f, start):
    bruh = [list(line.strip()) for line in f]
    set = {(start[0], start[
        1])}  # because there is no dups in a set saving cords is a good way to know if I have been there or not
    st = [start]  # the start of the stack
    while st:  # when it will pe empty it will finish
        y, x, w = st.pop()  # y,x cords and direction <>^v
        if not in_range(y, x, bruh): continue
        symbol = w + get_symbol(bruh, y, x)  # this is the combo's listed in the dictionary above
        if symbol in dire:
            for i in dire[symbol]:  # runs between 1 to 2
                y += dic[i][0]  # the expected y
                x += dic[i][1]  # expected x
                if not in_range(y, x, bruh): continue
                set.add((y, x))
                st.append((y, x, i))
                if get_symbol(bruh, y, x) in '^>.<v':
                    bruh[y][x] = i
        else:
            y = y + dic[w][0]  # increase the y to the place it should go
            x = x + dic[w][1]  # same
            if not in_range(y, x, bruh): continue  # if out of the range then fuck off
            if get_symbol(bruh, y, x) == w: continue  # if the current symbol is
            set.add((y, x))
            st.append((y, x, w))  # adds to the queue
            if get_symbol(bruh, y, x) in '^>.<v':
                bruh[y][x] = w
    return len(set)


def main(file):
    res = []  # took me much time but turns out the easy way of brute force is the way :(
    for i in range(len(file)):  # columns first and last one
        res.append(calculate(file, (i, 0, '>')))
        res.append(calculate(file, (i, len(file[0]), '<')))
    for i in range(len(file[0])):  # rows 0 and the end one
        res.append(calculate(file, (0, i, 'v')))
        res.append(calculate(file, (len(file[0]), i, '^')))
    print(max(res))  # 7943


from timeit import default_timer as timer

if __name__ == '__main__':
    with open('day16.txt') as f:
        start = timer()
        main(f.read().split('\n'))
        end = timer()
        print(end - start) #run time average of 3.1 seconds
