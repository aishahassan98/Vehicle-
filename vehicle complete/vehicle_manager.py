from vehicle import vehicle
import datetime
from car import Car
from truck import Truck
from bicycle import Bicycle

class vehicle_manager:
    def __init__(self,id,hire_date,return_date,available_trucks, available_cars, available_bicycles):
        super().__init__(id,hire_date,return_date)
     

class vehicleManager:
    def __init__(self,vehicles):
        self.vehicles_list = vehicles

def available_cars(self):
    available_cars = []
    for vehicle in self.vehicles_list:
                if isinstance(vehicle,Car) and vehicle.return_date < datetime.date.today():
                    available_cars.append(vehicle)
                    return available_cars

def available_trucks(self):
    available_trucks = []
    for vehicle in self.vehicles_list:
                if isinstance(vehicle,Truck) and vehicle.return_date < datetime.date.today():
                    available_trucks.append(vehicle)
                    return available_trucks

def available_bicycles(self):
    available_bicycles = []
    for vehicle in self.vehicles_list:
                if isinstance(vehicle,Bicycle) and vehicle.return_date < datetime.date.today():
                    available_bicycles.append(vehicle)
                    return available_bicycles

print(available_cars)