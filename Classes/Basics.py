class Student:
    name = "Mac"
    
me = Student()
print(me.name)

---------------------------
class Student:
    name = "Mac"
    def praise (self):
        return ("You're doing a great job {}".format(self.name))

--------------------------------
    
class Student:
    name = "Your Name"
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()
  
    
    -------------
    
    
class Student:
    name = "Your Name"
    
    def __init__(self,name,**kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()
        return self.reassurance()
    
    
    ------------------
    class RaceCar:
    
        def __init__(self, color, fuel_remaining, **kwargs):
            self.color = color
            self.fuel_remaining = fuel_remaining

            for key, value in kwargs.items():
                setattr(self, key, value)
                
       -------------
    class RaceCar:
    
        def __init__(self, color, fuel_remaining, laps=0, **kwargs):
            self.color = color
            self.fuel_remaining = fuel_remaining
            self.laps = laps
            

            for key, value in kwargs.items():
                setattr(self, key, value)
                
        def run_lap(self,length):
            self.fuel_remaining -=length *0.125
            self.laps +=1
