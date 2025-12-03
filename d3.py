with open('d3_input.txt', 'r') as f:
    x = f.read().split()
x = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

def part_1():
    joltage = []
    for l in x:
        big = 0
        nums = [int(b) for b in list(l)]
        for i,n in enumerate(nums):
            if i+1 == len(nums):
                break
            for t in nums[i+1:]:
                batt = n * 10 + t
                if batt > big:
                    big = batt
        joltage.append(big)
    print(sum(joltage))

# Part 1 - 16927 correct

def build(nums):
    i = 0
    batt = 0
    idx = 0
    #This logic works for test dataset, but not full dataset.
    # I think this while loop is valid to get the starting number
    while i+12 < len(nums): 
        if nums[i] > batt:
            batt = nums[i]
            idx = i
        i += 1
    new_nums = nums[idx:]
    # I think this loop is not using the right logic. It is removing the first smallest number.
    # However, 8345258111111 would be larger if the first 3 was removed and not the first 1
    # Furthermore, a number with many more digits afterwards would be best suited to remove as many numbers as possible to reach the largest next digit
    # 83452581111111111111111 > 88111111111
    # 83452581111111111119111 > 88111119111
    # The current logic will come up with 83452581111111111111111 > 834525811111
    # First Attempt
    # while len(new_nums) > 12:
    #     rem = min(new_nums)
    #     new_nums.remove(rem)
    """
    Need something that will take the length of the list into account and break once it is 12
    If the length is over 12, then remove any number between the starting digit and the next digit which is either the same or next largest in the remaining
    This logic works for the test case, but still too low on the full data.
    """
    #second attempt
    start = 1
    next_largest_idx = 0
    while len(new_nums) > 12:
        if start + 12 >= len(new_nums):
            print('asdfasdf')
        else:
            next_largest_idx = new_nums.index(max(new_nums[start:-12]),start)
        if next_largest_idx + 12 > len(new_nums) - start:
            rem = min(new_nums)
            new_nums.remove(rem)
            continue

        while start < next_largest_idx:
            new_nums.pop(start)
            next_largest_idx -= 1
        start += 1
    # Third attempt
    # while len(new_nums) > 12:
        """
        Start at index 1 since index 0 is always correct
        Get the next largest number in the rest of the list
            largest_number = max(new_nums[start:])
            next_largest_idx = new_nums.index(largest_number, start) # Start after last known valid number
        Check if this index + 12 is larger than the length of the list
            if next_largest_idx + 1, > len(new_nums) # - start?
            If it is, then find the next largest index
        """
    return int(''.join([str(x) for x in new_nums]))

joltage = []
for i,l in enumerate(x):
    nums = [int(n) for n in list(l)]
    jolt = build(nums)
    joltage.append(jolt)
print('\n'.join([str(n) for n in joltage]))
print("Sum: ", sum(joltage))
# Part 2    - 165591393734464 too low
# Part 2    - 167135271376171 too low
# Part 2    - 167279127055061 Wrong, no indication of high or low