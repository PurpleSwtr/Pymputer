class PC():
    def __init__(self):
        self.counter: int = 0
    
    def __repr__(self):
        return f'\n[PC] {self.counter}'
    
    def add(self):
        self.counter += 1

