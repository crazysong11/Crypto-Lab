#coding: utf-8

import hashlib
import base64
dic = '0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP'
for a in dic:
  for b in dic:
    for c in dic:
        for d in dic:
            s = str(a)+str(b)+str(c)+str(d)
            t = s + '9KwkldixoN8XaJGx'
            md5 = hashlib.md5(str(t).encode("utf-8")).hexdigest()
            if md5[:32] == '1e0561e4f778f7d6d1f4c249218526d2':
                print(t)