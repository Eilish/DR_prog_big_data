#### Name: Eilish Murphy
#### Number: 10190433
#### CA2 - DBS Car Rental Program

### DBSRental.py: Create Dealership Class and User Interface



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
        print '\n\tCurrent Stock:'
        print '\t\t%d Petrol Cars' %len(self.petrol_cars)
        print '\t\t%d Diesel Cars' %len(self.diesel_cars)
        print '\t\t%d Electric Cars' %len(self.electric_cars)
        print '\t\t%d Hybrid Cars' %len(self.hybrid_cars)
        
        
    def rent(self, car_list, required):
        if len(car_list) < required:
            print '\nThere is not enough cars in stock to fulfil rental\n'
            self.stock_count()
        else:
            count = 0
            while count < required:
                car_list.pop()
                count = count + 1
                
            print 'You have sucessfully rented %d cars' %required
        
    def restock(self, car_list, returned, Car):
        for i in range(returned):
            car_list.append(Car())
        print 'You have sucessfully returned %d cars' %returned    
    ## deal with trying to return to many cars!    
        
        
        
        
        
if __name__ == '__main__': 
    DBSRental = Dealership()  

    DBSRental.create_current_stock()
    
    print 'Welcome to DBS Car Rental\n'
    
    while True:
        mode = raw_input("Would you like to rent or return a car?\n\nPlease type '1' to rent or '2' to return\nType 'q' to quit> ")
        if mode == 'q':
            print 'Goodbye'
            quit()
        if mode == '1':
            while True:
                print 'What type of car would you like?\n'
                car_type = str.lower(raw_input("Please type\n'p' for a Petrol Car\n'd' for a Diesel Car\n'e' for an Electric Car\n'h' for a Hybrid Car:\n'n' for None and to exit\n> "))
                
                if car_type == 'n':
                    print 'Goodbye'
                    quit()
                
                required = raw_input('How many cars would you like?\n> ')
                try:
                    required = int(required)
                except:
                    continue
                
                if car_type == 'p':
                    DBSRental.rent(DBSRental.petrol_cars, required)
                    break
                elif car_type == 'd':
                    DBSRental.rent(DBSRental.diesel_cars, required)
                    print len(DBSRental.diesel_cars)
                    break
                elif car_type == 'e':
                    DBSRental.rent(DBSRental.electric_cars, required)
                    break
                elif car_type == 'h':
                    DBSRental.rent(DBSRental.hybrid_cars, required)
                    break
                else:
                    print "Selection must be 'p', 'd', 'e', 'h' or 'n', Try again"
                    continue    
        elif mode == '2':  
            while True:
                print 'What type of car are you returning?\n'
                car_type = str.lower(raw_input("Please type\n'p' for a Petrol Car\n'd' for a Diesel Car\n'e' for an Electric Car\n'h' for a Hybrid Car:\n'n' for None and to exit\n> "))
                
                if car_type == 'n':
                    print 'Goodbye'
                    quit()
                
                returned = raw_input('How many cars are you returning?\n> ')
                try:
                    returned = int(returned)
                except:
                    continue
                
                if car_type == 'p':
                    print 'yes'
                    DBSRental.restock(DBSRental.petrol_cars, returned, DBSRental.PetrolCar())
                    print len(petrol_cars)
                    break
                elif car_type == 'd':
                    DBSRental.restock(DBSRental.diesel_cars, returned, DBSRental.DieselCar())
                    break
                elif car_type == 'e':
                    DBSRental.restock(DBSRental.electric_cars, returned, DBSRental.ElectricCar())
                    break
                elif car_type == 'h':
                    DBSRental.restock(DBSRental.hybrid_cars, returned, DBSRental.HybridCar())
                    break
                
                else:
                    print "Selection must be 'p', 'd', 'e', 'h' or 'n', Try again"
                    continue    
        else:
            print 'You must select either 1, 2 or q'
            continue
            
                
            
    
    
    
    
    
        


     