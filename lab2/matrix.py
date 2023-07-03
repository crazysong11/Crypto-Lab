while True:
    n = int(input())
    k = input().strip().replace("\r\n", "")
    s = input().strip().replace("\r\n", "")
    mode = int(input())
    l = []
    ans = ""

    if mode == 1:
        for i in range(n):
            l.append([])
        for i in range(len(s)):
            l[i % n].append(s[i])
        for i in range(n):
            for j in range(n):
                if int(k[j]) == i + 1:
                    ans = ans + "".join(l[j])
                    break
        print(ans)

    else:
        for i in range(n):
            l.append("0")
        length = len(s) // n
        i = 0
        f = 0
        while True:
            for j in range(n):
                if int(k[j]) == f + 1:
                    l[j] = s[i:i + length]
                    f += 1
                    break
            if i + length != len(s):
                i = i + length
            else:
                break
        for i in range(length):
            for j in range(n):
                ans = ans + l[j][i]
        print(ans)

