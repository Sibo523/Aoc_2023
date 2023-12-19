mapy, instruction = open('day19.txt').read().split('\n\n')  # Split the map and instruction
dic = {key: line[:-1].split(',') for key, line in (i.split('{') for i in mapy.split('\n'))}
socially_accepted = []

def x_max(x, m, a, s):
    global dic
    cur = 'in'
    while True:
        if cur in 'RA':
            return cur == 'A'
        for i in dic[cur]:
            if ':' in i: #if I found
                val, to = i.split(':')
                if eval(val): #if it's true then I want to go where it tells me too so I break from the current instruction
                    cur = to
                    break
            elif i in 'RA':
                return i == 'A'
            else:
                cur = i



for instru in instruction.split('\n'):
    x, m, a, s = [int(variable.split('=')[-1]) for variable in instru[1:-1].split(',')]
    socially_accepted.append(x + m + a + s) if (x_max(x, m, a, s)) else None
print(sum(socially_accepted))
