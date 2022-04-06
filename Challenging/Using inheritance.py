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


class cargoShuttle(SpaceShip):  # cargoShuttle inheitance from SpaceShip
   def __init__(self):
        # instance variables 
        self.callSign = "cargo"   # string with empty defult value ( Overriding )
        self._shieldStrength = 50 # number with 50 as defult value ( Overriding )

        
abdo = cargoShuttle()
abdo.fireMissile()  # Pew Printed 