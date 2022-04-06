class SpaceShip():

    def __init__(self):
        # instance variables 
        self.callSign = ""   # string with empty defult value
        self._shieldStrength = 100 # number with 100 as defult value


     
     # Methods   
    def fireMissile(self):
        print (" Pew ")

    def reduceShield(self , amount):
        self.shieldStrength -= amount   


abdo = SpaceShip()
abdo.fireMissile()  # Pew Printed 