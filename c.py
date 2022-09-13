
def find(m,stepsMap):
    if m in stepsMap:
        return stepsMap[m]
        
    if(m == 1):
        stepsMap[m] = 0

    elif(m % 2 == 0):
        stepsMap[m] \
        = 1 \
           + find(m//2, stepsMap)
 
    else:
        stepsMap[m] \
        = 1 \
          + find(3 * m + 1, stepsMap)
     
    return stepsMap[m]
    

m = int(input())
stepsMap = {}
find(m,stepsMap)
print('m = ',m,' Number of Steps required = ',stepsMap[m])
