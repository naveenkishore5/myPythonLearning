import string

input1 = ['ab','cd','ef','gh','ij','kl','mn','op','qr','st','uv','wx','yz', 'abcd', 'efgh']
input2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4]


d = {}
res = 0
for i in range(len(input1)):
    if input2[i] in d:
        d[input2[i]].append(input1[i])
    else:
        d[input2[i]] = [input1[i]]

print(d)

alpha = set(string.ascii_lowercase)

for k, v in d.items():
    if k * len(v) == 26:
        print('yes', v)
        cs = ''
        for i in range(len(v)):
            cs += v[i]
        setOfValues = set(cs)
        if alpha.issubset(setOfValues):
            res += len(v)

    else:
        print('no', v)

print(res)






