import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config

class Auto_Data():
    def __init__(self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,width,height,
                 curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system):
        # self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive-wheels,engine-location,wheel-base,length,width,height,
                #  curb-weight,num-of-cylinders,engine-size,bore,stroke,compression-ratio,horsepower,peak-rpm,city-mpg,highway-mpg,make,body-style,engine-type,fuel-system
        
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.make = "make_" + make 
        self.body_style = "body-style_" + body_style
        self.engine_type = "engine-type_" + engine_type
        self.fuel_system = "fuel-system_" + fuel_system
        
        
    def load_model(self):
        with open(config.model_path,"rb")as f:
            self.model = pickle.load(f)
            
        with open(config.json_file_path,"r")as f:
            self.json_data = json.load(f) 
            
    def get_prediction(self):
        self.load_model()

        self.make_index = list(self.json_data['columns']).index(self.make)
        self.body_style_index = list(self.json_data['columns']).index(self.body_style)
        self.engine_type_index = list(self.json_data['columns']).index(self.engine_type)
        self.fuel_system_index = list(self.json_data['columns']).index(self.fuel_system)
        
        array = np.zeros(len(self.json_data["columns"]))
        array[0] = self.symboling
        array[1] = self.normalized_losses
        array[2] = self.json_data['fuel-type'][self.fuel_type]
        array[3] = self.json_data['aspiration'][self.aspiration]
        array[4] = self.json_data['num-of-doors'][self.num_of_doors]
        array[5] = self.json_data['drive-wheels'][self.drive_wheels]
        array[6] = self.json_data['engine-location'][self.engine_location]
        array[7] = self.wheel_base
        array[8] = self.length
        array[9] = self.width
        array[10] = self.height
        array[11] = self.curb_weight
        array[12] = self.json_data['num_of_cylinders'][self.num_of_cylinders]
        array[13] = self.engine_size
        array[14] = self.bore
        array[15] = self.stroke
        array[16] = self.compression_ratio
        array[17] = self.horsepower
        array[18] = self.peak_rpm
        array[19] = self.city_mpg
        array[20] = self.highway_mpg

        array[self.make_index] = 1
        array[self.body_style_index] = 1
        array[self.engine_type_index] = 1
        array[self.fuel_system_index] = 1
        
        price = round(self.model.predict([array])[0])
        return round(price, 2)
        
# if __name__ == "__main__":
    
#     symboling = 3.0 
#     normalized_losses = 115.0
#     fuel_type = "gas" 
#     aspiration = 'turbo'
#     num_of_doors = 'four'
#     drive_wheels = 'rwd'
#     engine_location = 'front'
#     wheel_base = 109.1
#     length = 188.8
#     width = 68.9
#     height = 55.5
#     curb_weight = 2952
#     num_of_cylinders = "five"
#     engine_size = 173
#     bore = 3.19
#     stroke = 2.87
#     compression_ratio = 10.6
#     horsepower = 3750
#     peak_rpm = 5500
#     city_mpg = 26.0
#     highway_mpg = 30.0 


#     make = "alfa-romero"


#     body_style = "hatchback"


#     engine_type = "ohc"

#     fuel_system = "spdi"
        

# pred = Auto_Data(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,width,height,
#                  curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)
# price = pred.get_prediction() 
# print("predicted car price --->",price)
        
                         
        
        
        
    