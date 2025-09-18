li =list(input().split())
# for i in range(0,len(li)):
#     if type(li[i]):
#         if float(li[i]) == int(li[i]):
#             li[i] = int(li[i])
#         else:
#             li[i] = float(li[i])
#print(li)
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
def unique_sorted(st):
    ln = []
    for i in range(0,len(st)):
        if float(st[i]) == int(float(st[i])):
            ln.append(int(float(st[i])))
        else:
            ln.append(float(st[i]))
    ln = set(ln).sort()
    return print(list(ln))
    