class SolveForM:
    
    @classmethod
    def get_next_val(cls, m):
        if m%2==0:
            return m/2
        else:
            # cm(n) ∗ 3 + 1
            return m*3+1

    def solve(self, m):
        n = 1
        next_value = m
        values_list = []
        while True:
            if next_value==1:
                return n,values_list
            n+=1
            next_value = self.get_next_val(next_value)
            values_list.append(next_value)

if __name__ == "__main__":
    m = int(input("Please enter the value of M to solve the equation upto value 1 => "))
    solver = SolveForM()
    n,values_list = solver.solve(m)
    print(f"No of steps for solving {m} => {n}")
    print(f"values list = {values_list}")