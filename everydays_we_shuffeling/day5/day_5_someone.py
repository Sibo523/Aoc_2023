from functools import reduce
import timeit

# Read input data from 'day_5.txt'
seeds, *mappings = open('day_5.txt').read().split('\n\n')

seeds = list(map(int, seeds.split()[1:]))

def lookup(inputs, mapping):
    """
    A generator function that performs memory lookups based on given inputs and memory mapping.

    Parameters:
    - inputs (list): List of tuples containing start positions and lengths to look up.
    - mapping (str): String representation of memory mapping rules.

    Yields:
    Tuple: Represents the result of the memory lookup (start position, length).
    """
    for start, length in inputs:
        print(f'{start = }')
        print(f'{length = }')
        while length > 0:
            for m in mapping.split('\n')[1:]:
                # Extract destination, source, and length from the mapping rule

                dst, src, len = map(int, m.split())
                # Calculate the difference between the start position and source position
                delta = start - src
                if delta in range(len):
                    # Adjust the length based on the delta, yielding the result
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else:
                # If no match is found in the mapping, yield the original input tuple
                yield (start, length)
                break

def main():
    """
    The main function that processes the input seeds and mappings to find the minimum memory position.

    Prints:
    The minimum memory positions for two sets of inputs:
    1. All seeds with a length of 1.
    2. Pairs of seeds where the first seed is used as the start position, and the second seed is the length.
    """
    # Perform memory lookups for two sets of inputs and print the minimum memory positions
    results = [min(reduce(lookup, mappings, s))[0] for s in [
        zip(seeds, [1] * len(seeds)),   # All seeds with a length of 1
        zip(seeds[0::2], seeds[1::2])   # Pairs of seeds as (start, length)
    ]]
    print(*results)

if __name__ == '__main__':
    # Measure the time taken to execute the main function and print the result
    print(f'Time took: {timeit.timeit(main, number=1)}')
