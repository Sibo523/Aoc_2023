

def Hash(line):
    total =0
    return [total := ((total +ord(i))*17)%256 for i in line][-1]



def main(file):
    print(sum(map(Hash, file)))

if __name__ == '__main__':
    with open ('day_15.txt') as file:
        main(file.read().split(','))