def FindSteps(m):
    steps = []
    i=1  
    count = 0
    if(m==1):
        return m
    last = m
    while True:
        if(last==1):
            print(f"For m = {m} : ")
            steps = list(map(str,steps))
            print("->".join(steps))
            print("\n")
            return count
        if i==1:
            last = m
            steps.append(last) 
        else:
            if(last %2 ==0):
                last = last//2
                steps.append(last)
            else:
                last = 3*last + 1
                steps.append(last)
        count+=1
        i+=1

for i in range(1,10001):
    FindSteps(i)






