
class backpage:
    def __init__(self, color, sizes, types):
        self.color = color
        self.sizes = sizes
        self.types = types
  
    def save(self):
        print("The backpage is saving objects")

    def transport(self):
        print("The backpage is transporting objects")
    
    def order(self):
        print("The backpage is ordering objects")

    def describe(self):
        print(f"This backpage is color {self.color}", f"size {self.sizes}", 
            f"and the type is {self.types}")
    
backpage1 = backpage("blue","big","school") 
backpage2 = backpage("red", "small", "sport")

print(backpage1.color)
print(backpage1.types)

backpage1.transport()
backpage2.describe()

print(backpage2.color)