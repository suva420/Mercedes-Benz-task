def find(m):
    stepCount = 0
    while m != 1:
        if m % 2 == 0:
           m = m // 2
           stepCount  += 1
        else:
            m = m * 3 + 1
            stepCount += 1
    return stepCount

for i in range(1,10001):
    print('m = ',i,' Number of Steps required = ',find(i))