import re, timeit


def endy(i, next_section, D):
    if i == len(next_section) - 1:
        return len(D)
    return next_section[i + 1] - 2

def found(section, end, D, seed):
    new_seed = []
    for tup_min, tup_max in seed:
        for line in range(section, end):  # goes over the lines to check
            res = [int(i) for i in D[line].split() if i.isdigit()]  # I now every line num
            maxi = res[1] + res[2]  # seed now is a tuple
            mini = res[1]
            dif = res[1] - res[0]
            if tup_min > maxi or tup_max < mini:
                seed.pop()
                new_seed.append((tup_min,tup_max))
                break  # break to the next tuple
            if mini <= tup_min <= tup_max <= maxi: # best case btw
                seed.pop()
                tup_max -= dif
                tup_min -= dif
                new_seed.append((tup_min,tup_max))
                break
            if tup_min < mini < maxi < tup_max:                       # Tuple spans the range, create three new tuples
                seed.pop()
                new_seed.append((mini-dif, maxi-dif))
                seed.append((tup_min, min(mini, tup_max)))
                seed.append((max(maxi, tup_min), tup_max))
                continue
            if tup_min < mini < tup_max < maxi:
                seed.pop()
                seed.append((tup_min, mini))
                new_seed.append((mini-dif,tup_max-dif))
                continue
            seed.pop()
            new_seed.append((tup_min-dif, maxi-dif))
            seed.append((maxi,tup_max))
    return new_seed


def main():
    with open('day_5.txt') as file:
        D = file.readlines()
        min_val = 10 ** 30
        next_section = []
        for index, i in enumerate(D[1:]):  # skip on the first line
            if i[0].isalpha():
                next_section.append(index + 2)  # know what line in the D we are :)
        res = [int(i) for i in D[0].split() if i.isdigit()]  # we have the seeds
        seed_tupple = [(res[i], res[i] + res[i + 1]) for i in range(0, len(res), 2)]  # tupples of ranges

        for seed_r in seed_tupple:  # runs on all seed ranges
            fml = [seed_r]
            for num_sec, section in enumerate(next_section):  # runs on every section
                end = endy(num_sec, next_section, D)  # gives the sections radius

                fml = found(section, end, D, fml)  # converts the seed to new thing
            kof = min(seed_tupple, key=lambda tup: tup[0])
            if (kof[0] < min_val): min_val = kof[0]  # update min_val after every number

        print(min_val)


if __name__ == '__main__':
    main()
    # print(f'time took: {timeit.timeit(main, number=1)}')
