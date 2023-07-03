w = 32
n = 624
m = 397
r = 31
a = 0x9908b0df
u = 11
d = 0xffffffff
s = 7
b = 0x9d2c5680
t = 15
c = 0xefc60000
l = 18
f = 0x6c078965

lower_mask = (1 << r) - 1
upper_mask = ~lower_mask

def seed_mt(seed):
    MT[0] = seed
    for i in range(1, n):
        MT[i] = (f * (MT[i - 1] ^ (MT[i-1] >> (w-2))) + i) & 0xffffffff

def twist():
    for i in range(n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if (x % 2) != 0:
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA

def extract_number():
    global index
    if index == 0:
        twist()

    y = MT[index]
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> l)

    index = (index + 1) % n
    return y & 0xffffffff

while True:
    index = 0
    MT = [0] * n
    seed = int(input())
    seed_mt(seed)
    for i in range(20):
        ans = extract_number()
        print(ans)