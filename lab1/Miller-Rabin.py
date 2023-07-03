import random

def MR(n):
    if n % 2 == 0 and n > 2:
        return False
    elif n == 2:
        return True
    else:
        k = -1
        while True:
            k += 1
            q = (n - 1) // int(pow(2, k))
            if q % 2 != 0:
                break

        for j in range(10):
            flag = 0
            x = 0
            a = random.randint(1, n - 1)
            if int(pow(a, q, n)) != 1:
                x = 1
            for i in range(k):
                if int(pow(a, q * pow(2, i), n)) == n - 1:
                    flag = 1
            if flag == 0 and x == 1:
                return False
        return True

x = int(input())
if (MR(x) == True):
    print("YES")
else:
    print("NO")