def find(list,key):
    counter = 0
    for i in list:
        if i == key:
            print(counter)
            break
        counter+=1
    return -1

find("amanuel","n")