"""
задача RLE необязательная. Реализуйте RLE алгоритм: 
реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
например декодирование
"""

def compression(s):
    mas = list(s)
    i=0
    res = []
    print(mas)
    while i<len(mas)-1:
        count = 1
        x = False
        for j in range(i+1, len(mas)):
            if mas[j] == mas[i]:
                count+=1
                i+=1 
            else:
                i+=1 
                if i == len(mas)-1:
                    x = True
                break
        res.append(str(count)+mas[i-1])
        if x == True:
            res.append("1"+mas[i])
    return("".join(res))

def restoring(s):
    mas = [s[i:i+2] for i in range(0, len(s), 2)]
    res = []
    for i in mas:
        n = int(i[0])
        c = i[1]
        for j in range(n):
            res.append(c)
    return(res)


comp = compression("aaabccccCCaB")
print(comp)        
print(restoring(comp))