
# for i in range(0,len(li)):
#     if type(li[i]):
#         if float(li[i]) == int(li[i]):
#             li[i] = int(li[i])
#         else:
#             li[i] = float(li[i])
#print(li)

#li = [3, -1, 5, 5, 0]
#li = [42] 
#li = [-5, -2, -9]
#li = []
#li = [1.5, 2, 2.0, -3.1]
def min_max(st):
    if len(st):
        ln = []
        for i in range(0,len(st)):
            if float(st[i]) == int(float(st[i])):
                ln.append(int(float(st[i])))
            else:
                ln.append(float(st[i]))
        return print(min(ln),max(ln))
    else:
        return print('ValueError')
#min_max(li)
#li = [3, 1, 2, 1, 3]
#li = []
#li = [-1, -1, 0, 2, 2]
#li = [1.0, 1, 2.5, 2.5, 0]
def unique_sorted(st):
    ln = []
    for i in range(0,len(st)):
        if float(st[i]) == int(float(st[i])):
            ln.append(int(float(st[i])))
        else:
            ln.append(float(st[i]))
    ln = list(set(ln))
    ln = sorted(ln)
    return print(ln)
#unique_sorted(li)
#li = [[1, 2], [3, 4]]
#li = ([1, 2], (3, 4, 5))
li = [[1], [], [2, 3]]
#li = [[1, 2], "ab"]
def flatten(st):
    st_itog = []
    for i  in st:
        if type(i) != str:
            for s in i :
                st_itog.append(s)
        else:
            return print('TypeError')
    return print(st_itog)
flatten(li)