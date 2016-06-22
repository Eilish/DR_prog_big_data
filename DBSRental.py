from DBSCars import PetrolCar, DieselCar, ElectricCar, HybridCar

class Dealership(object):

    def __init__(self):
        self.petrol_cars = []
        self.diesel_cars = []
        self.electric_cars = []
        self.hybrid_cars = []
        
    def create_current_stock(self):
        for i in range(24):
           self.petrol_cars.append(PetrolCar())
        for i in range(12):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())

    def stock_count(self):
        print 'There are %d petrol cars in stock' % len(self.petrol_cars)
        print 'There are %d diesel cars in stock' % len(self.diesel_cars)
        print 'There are %d electric cars in stock' % len(self.electric_cars)
        print 'There are %d hybrid cars in stock' % len(self.hybrid_cars)
        
    def rent(self, car_list, required):
        if len(car_list) < required:
            print 'There is not enough cars in stock to fulfil rental'
            print stock_count()
            return
        
        
            
        
            
            
            
        # total = 0
        # while total < amount:
           # car_list.pop()
           # total = total + 1

DBSDealership = Dealership()
DBSDealership.create_current_stock()
     