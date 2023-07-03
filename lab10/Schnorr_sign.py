import hashlib

p = int(input())
q = int(input())
a = int(input())
M = input()
mode = input().strip().replace('\r\n','')
if mode == 'Sign':
    x = int(input())
    k = int(input())
    r = pow(a, k, p)
    e = int(hashlib.sha1((M + str(r)).encode('utf-8')).hexdigest(), 16)
    s = (k + x * e) % q
    print("%d %d" % (e, s))
else:
    y = int(input())
    [e,s] = input().split()
    e = int(e)
    s = int(s)
    r1 = (pow(a,s,p) * pow(y,e,p)) % p
    if int(hashlib.sha1((M + str(r1)).encode('utf-8')).hexdigest(), 16) == e:
        print("True")
    else:
        print("False")