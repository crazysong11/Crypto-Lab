def gf_mult(a, b, poly):
    ans = 0
    digit_1 = poly.bit_length() - 1
    while b:
        if b & 1:
            ans = ans ^ a
        a, b = a << 1, b >> 1
        if a >> digit_1:
            a = a ^ poly
    return ans

while True:
    a = int(input(), 16)
    b = int(input(), 16)
    c = gf_mult(a, b, 0x11b)
    print(hex(c))