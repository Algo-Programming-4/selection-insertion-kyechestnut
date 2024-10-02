#bubble(list) - > sorted ist


#selection(list) -> sorted list

def selection (lis):
    length = len(lis)
    runs = 0
    min = 0
    cur =0
    temp =0
    
    while runs < length-1:
        min = runs
        cur = runs +1
        
        while cur < length:
            if lis[cur] < lis[min]:
                min = cur
            cur +=1
        if (min != runs):
            temp = lis[min]
            lis[min] = lis[runs]
            lis[runs] = temp
        runs += 1
    return lis
  
#insertion(list) > sorted list
