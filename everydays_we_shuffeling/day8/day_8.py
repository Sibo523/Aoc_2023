




def main(file): # remember to split ', ' for the keys to the next thing
    instruction, maper = file.split('\n\n')
    Dict = dict((x,y[1:-1]) for x,y in (line.split(' = ')
                for line in maper.split('\n')))
   
    cur = 'AAA'
    counter = 0
    real_counter =0
    while not 'ZZZ' == cur:
        ch = instruction[counter]
        left, right = Dict[cur].split(', ')
        cur = left if ch == 'L' else right
        counter = (counter + 1) % len(instruction)
        real_counter += 1
    print(real_counter)

if __name__ == '__main__':
    with open('day8.txt') as file:
        main(file.read())