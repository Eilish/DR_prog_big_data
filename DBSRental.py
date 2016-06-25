#### Name: Eilish Murphy
#### Number: 10190433
#### CA2 - DBS Car Rental Program

### DBSRental.py: Create Dealership Class and User Interface

from DBSCars import Car, PetrolCar, DieselCar, ElectricCar, HybridCar

# Create Dealership Object
class Dealership(object):

    def __init__(self):
        self.petrol_cars = []
        self.diesel_cars = []
        self.electric_cars = []
        self.hybrid_cars = []
        
    # function to create current stock
    def create_current_stock(self):
        for i in range(24):
           self.petrol_cars.append(PetrolCar())
        for i in range(12):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())

    # function to return current stock level
    def stock_count(self):
        return '\n\tCurrent Stock:\n\t\t%d Petrol Cars\n\t\t%d Diesel Cars\n\t\t%d Electric Cars\n\t\t%d Hybrid Cars\n' % (len(self.petrol_cars), len(self.diesel_cars), len(self.electric_cars), len(self.hybrid_cars))
        
        
    # function to process rental 
    def rent(self, car_list, required):
        if len(car_list) < required:
            return '\nThere are not enough cars in stock to fulfil rental\n%s' %self.stock_count()
            
        else:
            count = 0
            while count < required:
                car_list.pop()
                count = count + 1
                
            return 'You have successfully rented %d cars\n' %required
        
    # function to return rented vehicle
    def restock(self, car_list, returned, Car):
        for i in range(returned):
            car_list.append(Car())
        return 'You have successfully returned %d cars' %returned    
       
        
     # function to request car type from user
    def select_car_type(self):
        while True:
            car_type = str.lower(raw_input("Please type\n'p' for a Petrol Car\n'd' for a Diesel Car\n'e' for an Electric Car\n'h' for a Hybrid Car:\n'n' for None and to exit\n> "))
            if car_type == 'n':
                print 'Goodbye'
                quit()
            if car_type == 'p' or car_type == 'd' or car_type == 'e' or car_type == 'h':
                return car_type
                break
            else:
                print "Selection must be 'p', 'd', 'e', 'h' or 'n', Try again"
                continue
            
    # function to get number of cars from user
    def get_quantity(self):
        while True:    
            quantity = raw_input('How many cars?\n> ')
            try:
                quantity = int(quantity)
                return quantity
            except:
                print 'integer input only please'
                continue
    
        
if __name__ == '__main__': 
    
    # set up DBS Rental and create current stock 
    DBSRental = Dealership()  

    DBSRental.create_current_stock()
    
    print 'Welcome to DBS Car Rental\n'
    print DBSRental.stock_count()
    
    #get user to select rent/return mode
    while True:
        mode = raw_input("Would you like to rent or return a car?\n\nPlease type '1' to rent or '2' to return\nType 'q' to quit> ")
        if mode == 'q':
            print 'Goodbye'
            quit()
        
        # process rental
        if mode == '1':
            while True:
                print 'What type of car would you like?\n'
                
                car_type = DBSRental.select_car_type()
                
                required = DBSRental.get_quantity()
                                
                if car_type == 'p':
                    print DBSRental.rent(DBSRental.petrol_cars, required)
                    break
                if car_type == 'd':
                    print DBSRental.rent(DBSRental.diesel_cars, required)
                    break
                if car_type == 'e':
                    print DBSRental.rent(DBSRental.electric_cars, required)
                    break
                if car_type == 'h':
                    print DBSRental.rent(DBSRental.hybrid_cars, required)
                    break
                   
        
        #process return
        elif mode == '2':  
            while True:
                print 'What type of car are you returning?\n'
                
                car_type = DBSRental.select_car_type()
                
                returned = DBSRental.get_quantity()
                
                if car_type == 'p':
                    if (len(DBSRental.petrol_cars) + returned) > 24:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print DBSRental.restock(DBSRental.petrol_cars, returned, PetrolCar)
                    break
                if car_type == 'd':
                    if (len(DBSRental.diesel_cars) + returned) > 12:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print DBSRental.restock(DBSRental.diesel_cars, returned, DieselCar)
                    break
                if car_type == 'e':
                    if (len(DBSRental.electric_cars) + returned) > 4:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print DBSRental.restock(DBSRental.electric_cars, returned, ElectricCar)
                    break
                if car_type == 'h':
                    if (len(DBSRental.hybrid_cars) + returned) > 4:
                        print 'Please check type and quantity: exceeds max stock'
                        continue
                    print DBSRental.restock(DBSRental.hybrid_cars, returned, HybridCar)
                    break
                
                    
        else:
            print 'You must select either 1, 2 or q'
            continue
            
                
            
    
    
    
    
    
        


     