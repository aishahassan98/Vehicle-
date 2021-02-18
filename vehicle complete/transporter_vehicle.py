from vehicle import vehicle

class TransporterVehicle(vehicle):
    def __init__(self,id, hire_date,return_date,load_capacity):
        super().__init__(id,hire_date,return_date)
        self.load_capacity = load_capacity

bus = TransporterVehicle(5,34/5/3920,8/9/3030,2000)

