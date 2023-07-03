import hashlib
import random
import sys

n = int(input())
h = input().strip().replace('\r\n','')

num = n // 4

for c in range(32, 127):
    if hashlib.sha1(chr(c).encode('utf-8')).hexdigest()[0:num] == h[0:num]:
        print(chr(c))
        sys.exit(0)

for c in range(32, 127):
    for d in range(32, 127):
        if hashlib.sha1((chr(c)+chr(d)).encode('utf-8')).hexdigest()[0:num] == h[0:num]:
            print(chr(c)+chr(d))
            sys.exit(0)

for c in range(32, 127):
    for d in range(32, 127):
        for e in range(32, 127):
            if hashlib.sha1((chr(c)+chr(d)+chr(e)).encode('utf-8')).hexdigest()[0:num] == h[0:num]:
                print(chr(c)+chr(d)+chr(e))
                sys.exit(0)

ans = ''
while True:
    for i in range(5):
        a = random.randint(32, 126)
        ans += chr(a)
    for c in range(32, 126):
        for d in range(32, 126):
            for e in range(32, 126):
                ans = ans + chr(c) + chr(d) + chr(e)
                if hashlib.sha1(ans.encode('utf-8')).hexdigest()[0:num] == h[0:num]:
                    print(ans)
                    sys.exit(0)