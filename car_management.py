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
        CarManager.ALL_CARS.append({
            car_id : self. _id,
            car_make : self._make,
            car_model : self._model,
            car_year : self._year,
            car_mileage : self._mileage,
            car_services : self._services
        })

        


        pass
    pass