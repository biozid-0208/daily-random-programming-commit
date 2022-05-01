class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        if carType ==1 and self.slots[0] > 0:
            self.slots[0] -= 1
        elif carType ==2 and self.slots[1] > 0:
            self.slots[1] -= 1
        elif carType ==3 and self.slots[2] > 0:
            self.slots[2] -= 1
        else:
            return False
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)