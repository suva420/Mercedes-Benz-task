m_arr = []
steps_arr = [1]
import  plotly.express as px
def FindSteps(m):
    m_arr.append(m)
    steps = []

    i=1

    count = 0
    

    if(m==1):
        return m
 
    last = m

    while True:
 
        
        if(last==1):
            
            steps = list(map(str,steps))
            steps_length = len(steps)
            steps_arr.append(steps_length)
            

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
        

for i in range(1,10000):  
    FindSteps(i)

px.scatter(x = m_arr,y = steps_arr,labels={"x":"Numbers","y":"Steps"}).show()





