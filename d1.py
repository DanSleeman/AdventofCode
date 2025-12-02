
with open('d1_input.txt', 'r') as f:
    x = f.read().split()
# x = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".split()

start = 50

class Dial():
    def __init__(self, start):
        self.position = start
        self.password = 0
    def rotate(self, input):
        d = input[0]
        n = int(input[1:])
        full_revs = int(n / 100)
        rotate = n % 100
        if d == 'R':
            self.rotate_right(rotate)
        else:
            self.rotate_left(rotate)
        self.password += full_revs
    def rotate_right(self, n):
        new_pos = (self.position + n) % 100
        if new_pos == 0 :
            self.password += 1
        self.position = new_pos
    def rotate_left(self, n):
        new_pos = (self.position - n) % 100
        if new_pos == 0:
            self.password += 1
        self.position = new_pos

    def rotate_new(self, input):
        d = input[0]
        n = int(input[1:])
        passes = 0
        full_revs = int(n / 100)
        new_pos = self.position
        rotate = n % 100
        if d == 'R':
            new_pos += rotate
            if (new_pos % 100 < self.position and self.position > 0) or new_pos == 0:
                passes += 1
        else:
            new_pos -= rotate
            if (new_pos % 100 > self.position and self.position > 0) or new_pos == 0:
                passes += 1
        self.position = new_pos % 100
        self.password += full_revs
        self.password += passes
        # print(f'Input: {input} | New pos: {new_pos % 100} | Password: {self.password} | Full Revs: {full_revs} | Passes: {passes}')

d = Dial(start)
for r in x:
    d.rotate_new(r)
print(d.password)

# 6913 - Too High (Matches test data set)
# 6311 - Too low (Incorporated check for starting at zero) Didn't pass the test dataset though
# 6907 - Correct - There were SOME zero landings which were being counted twice.
