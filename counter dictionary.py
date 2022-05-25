from typing import Counter


def codic(list):
    all = set()
    prin = set()
    lst = []
    
    for i in list:  
        all.add(i)
    for j in all:
        counter = 0
        for k in list:
            if j == k:
                counter +=1
        add = str(j)+":"+str(counter)
        lst.append(add)
    
    return lst

    
print(codic(['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into','the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']))

