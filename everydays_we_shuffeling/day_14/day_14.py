


def main(file):
    lemur = [list(i) for i in (zip(*file))]
    print(lemur)
    total = 0
    for line in lemur:
            to = 0
            index = 0
            while index < len(lemur) :
                if line[index] == 'O':
                    line[index] = '.'
                    line[to] = 'O'
                    total += len(line) - to
                    to+=1
                elif line[index] == '#':
                    to = index+1
                index+=1

if __name__ == '__main__':
    with open('day_14.txt') as file:
        main(file.readlines())