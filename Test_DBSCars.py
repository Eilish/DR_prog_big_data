#### Name: Eilish Murphy
#### Number: 10190433
#### CA2 - DBS Car Rental Program

###  Test_DBSCars.py: Test functionality of Car Class and PetrolCar, DieselCar, ElectricCar, HybridCar objects

import unittest

from DBSCars import Car, PetrolCar, DieselCar, ElectricCar, HybridCar

## test the Car class functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        
    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.setColour('red') 
        self.assertEqual('red', self.car.getColour())
    
    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ford') 
        self.assertEqual('Ford', self.car.getMake())
        
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.setMileage(100) 
        self.assertEqual(100, self.car.getMileage())
    
## test the Petrol car class functionality
class TestPetrolCar(unittest.TestCase):

    def setUp(self):
        self.petrolcar = PetrolCar()
        
    def test_petrol_car_cylinders(self):
        self.assertEqual(4, self.petrolcar.getNumberCylinders())
        self.petrolcar.setNumberCylinders(5)
        self.assertEqual(5, self.petrolcar.getNumberCylinders())
        
## test the Diesel car class functionality
class TestDieselCar(unittest.TestCase):

    def setUp(self):
        self.dieselcar = DieselCar()
        
    def test_diesel_car_glow_plugs(self):
        self.assertEqual(4, self.dieselcar.getNumberGlowPlugs())
        self.dieselcar.setNumberGlowPlugs(5)
        self.assertEqual(5, self.dieselcar.getNumberGlowPlugs())        
        
## test the Electric car class functionality
class TestElectricCar(unittest.TestCase):

    def setUp(self):
        self.electriccar = ElectricCar()
        
    def test_electric_car_fuel_cells(self):
        self.assertEqual(1, self.electriccar.getNumberFuelCells())
        self.electriccar.setNumberFuelCells(2)
        self.assertEqual(2, self.electriccar.getNumberFuelCells())        
    
## test the Hybrid car class functionality
class TestHybridCar(unittest.TestCase):

    def setUp(self):
        self.hybridcar = HybridCar()
        
    def test_hybrid_car_second_fuel_source(self):
        self.assertEqual('', self.hybridcar.getSecondFuelSource())
        self.hybridcar.setSecondFuelSource('Petrol')
        self.assertEqual('Petrol', self.hybridcar.getSecondFuelSource()) 
    
if __name__ == '__main__':
    unittest.main()        