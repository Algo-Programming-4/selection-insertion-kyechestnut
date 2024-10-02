#bubble(list) - > sorted ist
def bubble (lis):
    length = len(lis)
    while length > 0:
        itterations =0
        x = 1
        while x < length:
            if lis[x] < lis[x-1]:
                nw = lis[x]
                lis[x] = lis[x-1]
                lis[x-1] = nw
            x+=1
            itterations +=1
        length-=1
    print(x)
    return lis


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
def insertion(lis):
    
    length = len(lis)
    cur = 1
    temp =0
    
    while cur < length:
        t = cur
        while lis[t] < lis[t-1]:
            temp = lis[t]
            lis [t] = lis[t-1]
            lis[t-1] = temp
            if t>1:
                t -=1
        cur +=1

    return lis

