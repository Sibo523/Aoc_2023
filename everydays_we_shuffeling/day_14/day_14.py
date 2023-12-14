


def main(file):
    lemur = list(map("".join, zip(*file))) #[list(i) for i in (zip(*file))]
    total = 0                              #this is what I had originally but no need to change the map
    for line in lemur: #now the columns are the lines
            to = 0
            index = 0
            while index < len(lemur) :
                if line[index] == 'O':
                    # line[index] = '.'
                    # line[to] = 'O'
                    total += len(line) - to #if found 'O' then add to the total with the place it should be (to)
                    to+=1 #to should increment to the next place that haves '.'
                elif line[index] == '#': #this is now a new block need to update where to direct the 'O'
                    to = index+1
                index+=1
    print(total)

if __name__ == '__main__':
    with open('day_14.txt') as file:
        main(file.readlines())