def binsearch(list,key):
    first = 0
    last = len(list)-1
   
    while first<last:
        mid = (first + last)//2
        if list[mid] == key:
            print(mid)
            break
        elif key < list[mid]:
            last = mid
        else:
            first = mid
    return False
binsearch([1,2,3,4,5,61,76],10)
    

    
    