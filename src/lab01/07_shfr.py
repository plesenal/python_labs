stroka = input()
stroka = stroka.split(".")[0]
itog_str = ""
frst_sim = 0
frst_num = 0
indx_first = 0
indx_secd = 0
for el in stroka:
    if el.isupper() and frst_sim == 0:
        frst_sim = 1
        itog_str += el
        indx_first = stroka.index(el)
    if el.isdigit() and frst_num == 0 and frst_sim != 0:
        indx_secd = stroka.index(el) + 1
        itog_str += stroka[indx_secd]
        frst_num = 1
step = int(indx_secd) - int(indx_first)
for i in range(indx_secd + step, len(stroka), step):
    itog_str += stroka[i]
print(itog_str + ".")
