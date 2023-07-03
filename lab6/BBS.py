if __name__ == '__main__':
    while True:
        len = int(input())
        p = int(input())
        q = int(input())
        s = int(input())
        n = p * q
        x0 = int(pow(s, 2, n))
        ans = ""
        for i in range(len):
            x1 = int(pow(x0, 2, n))
            b = x1 % 2
            ans = str(b) + ans
            x0 = x1
        print(int(ans,2))