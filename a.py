import time
def find(m):
    stepCount = 0
    while m != 1:
        if m % 2 == 0:
            m = m // 2
            stepCount += 1
        else:
            m = m * 3 + 1
            stepCount += 1
        print(m)
    return stepCount

t = time.time()
m = int(input())
print('m = ', m, ' Number of Steps required = ', find(m))
print(time.time() - t)