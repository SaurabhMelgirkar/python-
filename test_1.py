class paren1:
    def add(self,a,b):
        print(f"{a+b} ")
class parent2:    
        def add(self,a,b):
            super().add(a,b) 
            print(f"{a-b}")
            
class child(parent2,paren1):
    pass
c=child()
c.add(1,4)