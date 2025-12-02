# Part 1 - If the first and second half of the number are the same. I.E. 12341234; 11; 2020; - 23701357374 correct
# Part 2 - If an even split of the number has at least 2 repetitions of a pattern. I.E. 12341234; 123123123; 1111111 - 34284458938 correct
    # Smallest subset would be half of the string
    # Then 3 even groups if possible
    # Then 4, 5, 6, etc until group size of 1.
    # Get the factors of the length of the number. I.E. 10 > 1, 10, 5, 2 ; 6 > 1, 6, 3, 2
        # The factors cannot be greater than half of the string length. 10 > 1, 5, 2 only
    # For each factor, get a list of substrings of that length and check if they all match. If so, invalid product code.

with open('d2_input.txt', 'r') as f:
    x = f.read().split(',')
# x = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(',')
def part_1():
    s = 0
    for l in x:
        start, end = l.split('-')
        for n in range(int(start), int(end)+1):
            length = int(len(str(n))/2)
            f = str(n)[:length]
            e = str(n)[length:]
            if f == e:
                s += n
    print(f"Part 1: {s}")

def part_2():
    s = 0
    for l in x:
        start, end = l.split('-')
        # ls = len(start)
        # le = len(end)
        # sf = factors(ls)
        # ef = factors(le)
        # print(f'Start Length: {ls} | End Length: {le} | Start Factors: {sf} | End Factors: {ef}')
        for n in range(int(start), int(end)+1):
            l = len(str(n))
            f = factors(l)
            for c in f:
                chunked = chunk_list(str(n), c)
                if len(set(list(chunked))) == 1:
                    s += n
                    break
    print(f"Part 2: {s}")

def chunk_list(lst:list, chunk_size:int):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]
def factors(n):
    i = 1
    factors = []
    while i * 2 <= n:
        if n % i == 0:
            factors.append(i)
        i += 1
    return factors
part_1()
part_2()