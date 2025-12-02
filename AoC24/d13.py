import re
from math import gcd, ceil

with open('d13_input.txt', 'r') as f:
    x = f.read().strip()
TEST = True
TEST1 = 480
PART1 = 25751
TEST2 = None
PART2 = None

FIRST = True
if TEST:

    x = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

print(x)
machines = x.split('\n\n')
def machine_forumla(machine):
    a_pat = r'Button A: X\+(\d+), Y\+(\d+)'
    b_pat = r'Button B: X\+(\d+), Y\+(\d+)'
    p_pat = r'Prize: X=(\d+), Y=(\d+)'
    a = re.findall(a_pat, machine)[0]
    b = re.findall(b_pat, machine)[0]
    p = re.findall(p_pat, machine)[0]
    ax, ay = a
    bx, by = b
    x, y = p
    if FIRST:
        return (int(ax), int(bx), int(ay), int(by), int(x), int(y))
    return (int(ax), int(bx), int(ay), int(by), int(x)+10000000000000, int(y)+10000000000000)

def find_solutions(ax, bx, ay, by, x, y):
    # X position calculation
    max_x = ceil(x/min(ax, bx))
    max_y = ceil(y/min(ay,by))
    x_counts = []
    for X in range(max_x):
        for Y in range(max_y):
            if ax*X + bx*Y == x:
                print(f"X = {X}, Y = {Y}")
                x_counts.append((X,Y))
    valid_counts = []
    # Y position checks
    for xc in x_counts:
        X, Y = xc
        if ay*X + by*Y == y:
            print(f"Valid combination: {xc}")
            valid_counts.append(xc)
    return valid_counts

def find_cheapest(solutions):
    if not solutions:
        return 0
    return min([a * 3 + b * 1 for a,b in solutions])

def pre_validate(ax, bx, ay, by, x, y):
    gx = gcd(ax, bx)
    if x % gx != 0:
        return False
    gy = gcd(ay, by)
    if y % gy != 0:
        return False
    return ax // gx, bx // gx, ay // gy, by // gy, x // gx, y // gy
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return g, x, y

tokens = 0
for m in machines:
    f = machine_forumla(m)
    f = pre_validate(*f)
    if not f:
        continue
    _, x0, y0 = extended_gcd(f[0], f[1])
    v = find_solutions(*f)
    tokens += find_cheapest(v)
    print(v)
print(f"Part 1: {tokens}")

