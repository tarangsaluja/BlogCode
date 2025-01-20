class Squarednumber:
    def __init__(self, number, perfect):
        self.number = number
        self.perfect = perfect
    
    def binarySearch(self, iters):
        if self.perfect == False:
            print(binSearchIrrational(self.number, iters))
        else:
            print(binSearchRational(self.number))
    
    def binSearchIrrational(value, iters):
        return 0
    
    def binSearchRational(value):
        return 0




    

