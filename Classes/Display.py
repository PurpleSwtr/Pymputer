# Просто набросок того как может выглядеть дисплей нашего уже получается мини пк
# Не будем же мы принтить с помощью стандартного принт, верно....? 

class Display():
    
    def __init__(self,):
        self.x_size = 32
        self.y_size = 12

    def draw(self):
        for y in range(self.y_size):
            print()
            for x in range(self.x_size):
                print("-", end="")

ds = Display()
ds.draw()
        