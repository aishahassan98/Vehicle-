from transporter_vehicle import TransporterVehicle

class Truck(TransporterVehicle):
    def __init__(self,id, hire_date,return_date,load_capacity,num_of_axles):
        super().__init__(id, hire_date, return_date, load_capacity)
        self.num_of_axles = num_of_axles