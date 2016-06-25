#### Name: Eilish Murphy
#### Number: 10190433
#### CA2 - DBS Car Rental Program

###  Test_DBSRental.py: Test functionality of Dealership Object

import unittest
import mock

from DBSRental import Dealership
from DBSCars import Car, PetrolCar, DieselCar, ElectricCar, HybridCar

## test the Dealership class functionality
class TestDealership(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealership()
        self.dealer.create_current_stock()
        
        
    # test create current stock functionality
    # should create 24 petrol cars, 12 diesel cars, 4 electric cars and 4 hybrid cars
    def test_create_current_stock(self):
        self.assertEqual(24, len(self.dealer.petrol_cars))
        self.assertEqual(12, len(self.dealer.diesel_cars))
        self.assertEqual(4, len(self.dealer.electric_cars))
        self.assertEqual(4, len(self.dealer.hybrid_cars))
        
    # test stock count function 
    # return should be '\n\tCurrent Stock:\n\t\t%d Petrol Cars\n\t\t%d Diesel Cars\n\t\t%d Electric Cars\n\t\t%d Hybrid Cars\n' % (len(self.petrol_cars), len(self.diesel_cars), len(self.electric_cars), len(self.hybrid_cars))
    def test_stock_count(self):
        result = '\n\tCurrent Stock:\n\t\t%d Petrol Cars\n\t\t%d Diesel Cars\n\t\t%d Electric Cars\n\t\t%d Hybrid Cars\n' % (len(self.dealer.petrol_cars), len(self.dealer.diesel_cars), len(self.dealer.electric_cars), len(self.dealer.hybrid_cars))
        self.assertEqual(result, self.dealer.stock_count())
    
        
    # test rent function when car stock exceeds vehicles required
    # rent 2 cars from each type and check remaining stock 
    # remaining should be 22 petrol, 10 diesel, 2 electric, and 2 hybrid
    # return should equal 'You have successfully rented %d cars\n' %required
    def test_rent_cars_available(self):
        required = 2
        result = 'You have successfully rented %d cars\n' %required
        
        self.dealer.rent(self.dealer.petrol_cars, required)
        self.assertEqual(22, len(self.dealer.petrol_cars))
        self.assertEqual(result, self.dealer.rent(self.dealer.petrol_cars, required))
        
        self.dealer.rent(self.dealer.diesel_cars, required)
        self.assertEqual(10, len(self.dealer.diesel_cars))
        self.assertEqual(result, self.dealer.rent(self.dealer.diesel_cars, required))
                
        self.dealer.rent(self.dealer.electric_cars, required)
        self.assertEqual(2, len(self.dealer.electric_cars))
        self.assertEqual(result, self.dealer.rent(self.dealer.electric_cars, required))
               
        self.dealer.rent(self.dealer.hybrid_cars, required)
        self.assertEqual(2, len(self.dealer.hybrid_cars))
        self.assertEqual(result, self.dealer.rent(self.dealer.hybrid_cars, required))
    
    # test rent function when car stock is less than vehicles required
    # rent 50 cars from each type and check return = '\nThere are not enough cars in stock to fulfil rental\n'
    def test_rent_cars_not_available(self):
        result = '\nThere are not enough cars in stock to fulfil rental\n%s' % self.dealer.stock_count()
        self.assertEqual(result, self.dealer.rent(self.dealer.petrol_cars, 50))
        self.assertEqual(result, self.dealer.rent(self.dealer.diesel_cars, 50))
        self.assertEqual(result, self.dealer.rent(self.dealer.electric_cars, 50))
        self.assertEqual(result, self.dealer.rent(self.dealer.hybrid_cars, 50))
        
    # test restock function
    # return 2 cars to each type and check stock balance
    # len(list) after return should be petrol 26, diesel 14, electric 6, and hybrid 6
    # return should be 'You have successfully returned %d cars' %returned
    def test_restock(self):
        returned = 2 
        result = 'You have successfully returned %d cars' %returned
        
        self.dealer.restock(self.dealer.petrol_cars, returned, PetrolCar)
        self.assertEqual(26, len(self.dealer.petrol_cars))
        self.assertEqual(result, self.dealer.restock(self.dealer.petrol_cars, 2, PetrolCar))
        
        self.dealer.restock(self.dealer.diesel_cars, returned, DieselCar)
        self.assertEqual(14, len(self.dealer.diesel_cars))
        self.assertEqual(result, self.dealer.restock(self.dealer.diesel_cars, 2, DieselCar))
        
        self.dealer.restock(self.dealer.electric_cars, returned, ElectricCar)
        self.assertEqual(6, len(self.dealer.electric_cars))
        self.assertEqual(result, self.dealer.restock(self.dealer.electric_cars, 2, ElectricCar))
        
        self.dealer.restock(self.dealer.hybrid_cars, returned, HybridCar)
        self.assertEqual(6, len(self.dealer.hybrid_cars))
        self.assertEqual(result, self.dealer.restock(self.dealer.hybrid_cars, 2, HybridCar))

    # test get quantity function
    def test_get_quantity(self):
        with mock.patch('__builtin__.raw_input', return_value = '2'):
            assert self.dealer.get_quantity() == 2
        
    # test select car type function returns correct car_type
    def test_select_car_type(self):
        with mock.patch('__builtin__.raw_input', return_value = 'p'):
            assert self.dealer.select_car_type() == 'p'
        with mock.patch('__builtin__.raw_input', return_value = 'd'):
            assert self.dealer.select_car_type() == 'd'
        with mock.patch('__builtin__.raw_input', return_value = 'e'):
            assert self.dealer.select_car_type() == 'e'
        with mock.patch('__builtin__.raw_input', return_value = 'h'):
            assert self.dealer.select_car_type() == 'h'
        


if __name__ == '__main__':
    unittest.main()         