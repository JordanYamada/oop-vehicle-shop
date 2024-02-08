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
    print('-------------------\n-------------------\n----  WELCOME  ----\n-------------------\n-------------------')
    input(f'Enter any key to continue\n------------------>')
    car_terminal()

# Make a function to start the terminal interface
def car_terminal():
    user_input = input(f"What would you like to do?\n-------------------\nPlease Enter a Number\n-------------------\n1. Add a car\n2. View all cars\n3. View total number of cars\n4. See a car's details\n5. Service a car\n6. Update mileage\n---Enter 'Q' to Quit\n------------------>")
    match user_input:
        case '1':
            add_car()
        case '2':
            view_cars()    
        case 'Q'|'q':
            quit(user_input)
        case _:
            print('-----------\nInvalid choice\n-----------')
            car_terminal()    


# 1. Add a car
# def add_car():
#     make = input(f"What is your vehicle's make?")
#     quit(make) 
#     while bool(make) == False:
#         make = input(f"You did not enter a make.\nWhat is your vehicle's make?")
#         quit(make)

#     model = input(f"What is your vehicle's model?")
#     quit(model)

#     while type(model) != str:
#         model = input(f"You did not enter a model.\nWhat is your vehicle's model?")
#         quit(model)
#     # try:
#         year = input(f"What is your vehicle's year?")
#     # except:     
#     quit(year)
    # while type(year) == str or int(year) < 1900 or int(year) > 2024:
    #     year = input(f"You did not enter valid year.\nWhat is your vehicle's year?")
    #     quit(year)
    # mileage = input(f"What is your vehicle's mileage?")
    # quit(mileage)
    # while type(mileage) == str or mileage != '0':
    #     mileage = int(input(f"You did not enter valid mileage.\nWhat is your vehicle's mileage?"))
    #     quit(mileage)
    # new_car = CarManager(make, model, year, mileage)
    # print(f'Your vehicle has been added!\n{new_car}')
    # welcome()
            
def add_car():
    option_dict = {
        'make': '',
        'model': '',
        'year': 0,
        'mileage': 0,
    }
    for option in option_dict:
        match option:
            case 'make':
                ask_input(option,option_dict)
                validate_str(option, option_dict)

            case 'model':
                ask_input(option,option_dict)
                validate_str(option, option_dict)


            case 'year':
                # print('fired')
                ask_input(option,option_dict)
                validate_year(option,option_dict)


            case 'mileage':
                # print('fired')
                ask_input(option,option_dict)
                validate_int(option,option_dict)




# function to ask the user for their vehicle's information
def ask_input(key, dict):
    user_input = input(f"What is your vehicle's {key}?")
    dict[key] = user_input
    return dict

# funtion that checks to make sure the user does not input an empty string
def validate_str(key, dict):
    while bool(dict[key]) == False:
        print(f'You did not enter a {key}.')
        ask_input(key, dict)
    return dict

#funtion that checks to make sure the user enters a valid int response
def validate_int(key, dict):
    validate_str(key, dict)
    try:
        value = int(dict[key])
    except ValueError:
        print(f"Oops! That was not a valid {key}.\nPlease enter a valid {key}")
        ask_input(key, dict)
        validate_int(key, dict)
    else:
        dict[key] = value
        return dict
    
#function that checks to make sure the user enters a valid year
def validate_year(key, dict):
    validate_int(key, dict)

    while dict[key] < 1908 | dict[key] > 2024:
        print(f"Oops! That was not a valid {key}.\nPlease enter a valid {key} between 1908 and 2024")
        ask_input(key, dict)
        validate_year(key, dict)

    return dict


    # if bool(dict[key]) == False:
    #     print(f'You did not enter a valid {key}.')
    # return bool(dict[key])



    


# def is_valid_make(make):
#     while
#     pass

# def is_valid_model(model):
#     pass

# def get_make():
#     make = input("What is your make?")
#     try:
#         casted_make = int(make)
#         return casted_make
#     except:
#         return None

# def add_car_two():
#     get_car_details = [
    
#        [get_model, is_valid_model],
#         # etc ...
#     ]

#     for get_car_detail in get_car_details:
#         get_thing = get_car_detail[0]
#         validate_thing = get_car_detail[1]
        
#         is_valid = False

#         while(is_valid is False):
#             thing = get_thing()
#             is_valid = validate_thing(thing)

#         # do stuff with thing to save it hwoever now that its validated




# 2. View all cars
def view_cars():
    for car in CarManager.ALL_CARS:
        print(car)
    user_input = input('Enter any key to continue')
    if user_input:
        car_terminal()    
# 3. View total number of cars
# 4. See a car's details
# 5. Service a car
# 6. Update mileage
# 7. Quit
def quit(user_input):
    user_input = str(user_input)
    if user_input.lower() == 'q':
        welcome()
    else:
        return
    



car1 = CarManager('Tesla', 'Cyber Truck', 2026, 0)
print(CarManager.ALL_CARS)
print(car1)
welcome()