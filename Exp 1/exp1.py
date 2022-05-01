import sys
sys.setrecursionlimit(int(1e+6))

import itertools as it

def strip(txt):
    return txt.strip()

inp = dict()
with open('testcase2.txt', 'r') as f:
    for line in f.readlines():
        temp = list(map(strip, line.split('->')))
        inp[temp[0]] = list()
        for r in temp[1].split('|'):
            inp[temp[0]].append(tuple(r.split()))
# print(f"{inp}\n")

fst = dict()
flw = {list(inp.keys())[0]:['$']}
# print(flw)

def parser(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        while type(res[0]) == type(list()):
            res = res[0]
        return res
    return wrapper

@parser
def first(nt):
    res = list()
    temp = inp[nt]
    for prod in temp:
        k = 0
        while True:
            if k<len(prod):
                if 65 <= ord(prod[k][0] if len(prod[k])>1 else prod[k]) <= 90:
                    temp = first(prod[k])
                    if '#' in temp:
                        temp.remove('#')

                        res.append(temp)
                        k+=1; continue
                    else: res.append(temp); break
                else: res.append(prod[k]); break
            else: res.append('#'); break
    return res

def follow(nt):
    res = list()
    for v, prods in inp.items():
        for prod in prods:
            for i in range(len(prod)):
                if nt == prod[i]:
                    if i != len(prod)-1:
                        k = 1
                        while True:
                            if i+k<len(prod):
                                if 65 <= ord(prod[i+k][0] if len(prod[i+k])>1 else prod[i+k]) <= 90:
                                    temp = fst[prod[i+k]].copy()
                                    if '#' in temp: 
                                        temp.remove('#')
                                        res.append(temp)
                                        k+=1; continue
                                    else:
                                        res.append(temp); break
                                else: res.append(prod[i+k]); break
                            else:
                                if nt != v:
                                    if v not in flw.keys(): res.append(follow(v))
                                    else: res.append(flw[v])
                                    break
                                else: break
                    else:
                        if nt != v:
                            if v not in flw.keys(): res.append(follow(v))
                            else: res.append(flw[v])
    return res

for i in inp.keys():
    fst[i] = first(i)

for i in inp.keys():
    if i == list(inp.keys())[0]: flw[i].extend(list(set(it.chain.from_iterable(follow(i)))))
    else: flw[i] = list(set(it.chain.from_iterable(follow(i))))   # Temporary soln, fix it !

print('First:')
for k,v in fst.items():
    print(f"{k:{2}}: {v}")

print('\nFollow:')
for k,v in flw.items():
    print(f"{k:{2}}: {v}")


'''
'#'-> epsilon
Capital Letters -> Variables
'''
