class Rectangle ():
    #def __init__(self):
     #   self.width = 12
      #  self length  = 6
    def __init__(self, width, length ):
        self.width = width
        self.length  = length 
    #def __init__(self, NewRectangle):
      #  self.width = NewRectangle.width
       # self length  = NewRectangle length 
    def Perimeter (self):
       print("the perimeter is  {}".format((self.length +self.width)*2))

    def Air (self):
        print("the air is  {}".format(self.length *self.width))

    def Iscarre (self):
        if self.width == self.length :
            print("it is a square .")
        else:
            print("it is not a square .")

    def info (self):
        print(f"Length: {self.length }")
        print(f"width: {self.width}")
        self.Perimeter()
        self.Air()
        self.Iscarre()
    