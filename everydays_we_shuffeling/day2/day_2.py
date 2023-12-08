



import timeit
from collections import defaultdict

def main():
    with open('C:\\temp\\day2.txt') as f:
        D = f.read().strip()
        ans = 0
        for line in D.split('\n'):
            ok = True
            id,line = line.split(':')
            V = defaultdict(int)
            for event in line.split(';'):
                for balls in event.split(','):
                    n,color = balls.split()
                    n = int(n)
                    V[color] = max(V[color],n)
                  #      ok = False
            score = 1
            for v in V.values():
                score*=v
            ans+=score

            if ok:
                print(ans)
                pass
        print (ans)

if __name__ == "__main__":
    print(f'time took: {timeit.timeit(main, number=1)}')