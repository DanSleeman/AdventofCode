from collections import deque
with open('d3_input.txt', 'r') as f:
    x = f.read().split()
test = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
 ] # Part 2 answer = 3121910778619

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
    # while i+12 < len(nums): 
    #     if nums[i] > batt:
    #         batt = nums[i]
    #         idx = i
    #     i += 1
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
    start = 0
    next_largest_idx = 0
    N = 12
    L = len(nums)
    idx = 0
    "idx:L-N+n+1"
    while len(new_nums) > 12:
        end = len(new_nums) - 10
        if start >= end:
            rem = min(new_nums)
            new_nums.remove(rem)
            continue
        # if start + 12 >= len(new_nums):
        #     print('asdfasdf')
        # else:
        next_largest_idx = new_nums.index(max(new_nums[start:end]),start)
        # if next_largest_idx + 12 > len(new_nums) - start:
        #     rem = min(new_nums)
        #     new_nums.remove(rem)
        #     continue

        while start < next_largest_idx:
            new_nums.pop(start)
            next_largest_idx -= 1
        print(''.join([str(x) for x in new_nums]))
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

# Part 2 attempt 3
def deq(nums):
    new_nums = []
    N = 12
    L = len(nums)
    idx = 0
    while len(new_nums) < N:
        "idx:L-N+n+1"
        end = L - N + len(new_nums) + 1
        largest_num = max(nums[idx:end])
        idx = nums.index(largest_num,idx) + 1
        new_nums.append(largest_num)
    return int(''.join([str(x) for x in new_nums]))
def calc_jolt(input_list):
    joltage = []
    for i,l in enumerate(input_list):
        nums = [int(n) for n in list(l)]
        # jolt = build(nums)
        jolt = deq(nums)
        joltage.append(jolt)
    
    return joltage
    
j = calc_jolt(x)
print('\n'.join([str(n) for n in j]))
print("Puzzle Sum: ", sum(j))
testj = calc_jolt(test)
print("Test Sum: ", sum(testj))
print(f"Test Match? {3121910778619==sum(testj)}")
# Part 2    - 165591393734464 too low
# Part 2    - 167135271376171 too low
# Part 2    - 167279127055061 Wrong, no indication of high or low
# Part 2    - 167282215013591 Wrong, no indication of high or low
# Part 2    - 167301086469058 Wrong, no indication of high or low
# Part 2    - 167334875666958 Wrong, no indication of high or low
# Part 2    - 166668682236575 Wrong, Assumed too low
# Part 2    - 167384358365132 Correct - Help from subreddit