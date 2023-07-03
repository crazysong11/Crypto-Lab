import copy

t = []
for i in range(26):
    t.append(0)

s = input().strip().replace('\r\n','')
for c in s:
    t[ord(c)-ord('a')] += 1

max = 0
x = copy.deepcopy(t)
t.sort(reverse=True)
for i in range(26):
    if x[i] == t[0]:
        print((i+ord('a')+26-ord('e'))%26)