from passenger_vehicle import PassengerVehicle

class Bicycle(PassengerVehicle):
    def __init__(self,id, hire_date,return_date,max_num_of_passengers,num_of_doors, classification):
        super().__init__(id, hire_date,return_date,max_num_of_passengers)
        self.classification = classification

        classification = ["mountain", "eletric", "folding", "road"]

        

        
        