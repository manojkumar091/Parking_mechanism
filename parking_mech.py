import json 

class parking_algorithm:
    # JSON object holding the parking status data 
    parking_dict = {'parking_spot1':1,
        'parking_spot2': None,
        'parking_spot3': None
    } 
    # run time paramter holding the list of vehicle numbers to be parked
    vehicle_numbers = [1,2,3,4,5,6]

    # parked vehicles list
    parked_list = [1]

    def parking_mech(self):
        for vehicle in self.vehicle_numbers:
            #Check for the parking capacity
            if None in self.parking_dict.values():
                if vehicle in self.parked_list:
                    # if the vehicle is parked it will be excited
                    print('vechicle {} is already available in the parking slot and will be exited'.format(vehicle))
                    #exit the vehicle from the parking
                    self.parked_list.remove(vehicle)
                    for k,y in self.parking_dict.items():
                        if y == vehicle:
                            #updating the dictionary to fill up the empty space in the parking slot
                            self.parking_dict.update({k:None})
                            break
                else:
                    self.parked_list.append(vehicle) 
                    #adding the parked vehicle to the parkedlist
                    for k,y in self.parking_dict.items():
                        if y is None:
                            self.parking_dict.update({k:vehicle})
                            #updating the JSON with the newly added vehicle details
                            break
            else:
                print('Parking is full and cannot accomodate any other vehicles') 
                break
        #please provide the exact local location of the XML file 
        with open("parking_json.json", "w") as outfile:   
            json.dump(self.parking_dict, outfile)
        print('parking space',self.parking_dict)

vehicle_parking = parking_algorithm()

vehicle_parking.parking_mech()