# _id (instance attribute): An integer that should never be repeated and only rise with each car instance
# _make (instance attribute): A string representing the make of the car.
# _model (instance attribute): A string representing the model of the car.
# _year (instance attribute): An integer representing the manufacturing year of the car.
# _mileage (instance attribute): An integer representing the vehicles total mileage
# _services (instance attribute): A list that will store the services done to the car.


class CarManager:
    ALL_CARS = []
    TOTAL_CARS = 0
    INDEX = 1
    def __init__(self, make, model, year, mileage):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = []
        self._id = CarManager.INDEX

        CarManager.INDEX += 1
        CarManager.TOTAL_CARS += 1
        CarManager.ALL_CARS.append(
            {
                'id' : self. _id,
                'make' : self._make,
                'model' : self._model,
                'year' : self._year,
                'mileage' : self._mileage,
                'services' : self._services
            }
        )

    def __str__(self):
        return f'Id: {self._id}\nMake: {self._make}\nModel: {self._model}\nYear: {self._year}\nMileage: {self._mileage}\nServices: {self._services}'
    
    def __repr__(self):
        return str(self)


        pass
    pass

# ----  WELCOME  ----
def welcome():
    print('----  WELCOME  ----')
    user_input = input(f'Enter any key to continue')
    if user_input:
        car_terminal()

# Make a function to start the terminal interface
def car_terminal():
    user_input = input(f"What would you like to do?\n-----------\nPlease Enter a Number\n-----------\n1. Add a car\n2. View all cars\n3. View total number of cars\n4. See a car's details\n5. Service a car\n6. Update mileage\n---Enter 'Q' to Quit")


# 1. Add a car
def add_car():
    make = input(f"What is your vehicle's make?")
    quit(model)
    while type(make) != str:
        make = input(f"You did not enter a make.\nWhat is your vehicle's make?")
        quit(make)
    model = input(f"What is your vehicle's make?")
    quit(model)
    while type(model) != str:
        model = input(f"You did not enter a model.\nWhat is your vehicle's model?")
        quit(model)
    year = input(f"What is your vehicle's year?")
    quit(year)
    while type(int(year)) != int or int(year) < 1900 or int(year) > 2024:
        year = int(input(f"You did not enter valid year.\nWhat is your vehicle's make?"))
        quit(year)
    mileage = input(f"What is your vehicle's mileage?")
    quit(mileage)
    while type(int(mileage)) != int or mileage != '0':
        mileage = int(input(f"You did not enter valid mileage.\nWhat is your vehicle's mileage?"))
        quit(mileage)
    new_car = CarManager(make, model, year, mileage)
    print(f'Your vehicle has been added!\n{new_car}')
    welcome()
    

# 2. View all cars
def view_cars():
    for car in CarManager.ALL_CARS:
        print(car)
    user_input = input('Enter any key to continue')
    if user_input:
        welcome()    
# 3. View total number of cars
# 4. See a car's details
# 5. Service a car
# 6. Update mileage
# 7. Quit
def quit(user_input):
    if user_input.lower() == 'q':
        welcome()
    else:
        return
    



car1 = CarManager('Tesla', 'Cyber Truck', 2026, 0)
print(CarManager.ALL_CARS)
print(car1)
welcome()