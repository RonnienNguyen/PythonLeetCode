class Input(object):
    def __init__(self):
        self.s = ""    
    def getString(self):
        self.s = input("Input String")
    def printString(self):
        print(self.s.upper())
        
newStr = Input()
newStr.getString()
newStr.printString()
    