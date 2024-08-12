<<<<<<< HEAD
class Vehicle:
    def __init__(self,max_speed,mileage):
        self._maxspeed = max_speed;
        self._mileage = mileage;
    def fair_charge(self,seating_capacity):
        return seating_capacity * 100;

class Bus(Vehicle):
    def fair_charge(self,seating_capacity):
        total_fare = super().fair_charge(seating_capacity)
        maintenance = total_fare * 0.10
        return total_fare + maintenance
a1 = Vehicle(75,25)
a2 = Bus(75,25)
print(f"Seating capacity of Vehicle is {a1.fair_charge(25)}")
print(f"Seating capacity of Bus is {a2.fair_charge(25)}")
=======
class Vehicle:
    def __init__(self,max_speed,mileage):
        self._maxspeed = max_speed;
        self._mileage = mileage;
    def fair_charge(self,seating_capacity):
        return seating_capacity * 100;

class Bus(Vehicle):
    def fair_charge(self,seating_capacity):
        total_fare = super().fair_charge(seating_capacity)
        maintenance = total_fare * 0.10
        return total_fare + maintenance
a1 = Vehicle(75,25)
a2 = Bus(75,25)
print(f"Seating capacity of Vehicle is {a1.fair_charge(25)}")
print(f"Seating capacity of Bus is {a2.fair_charge(25)}")
>>>>>>> f4e2c28e162fb5654aa5dc826812270fccec2216
