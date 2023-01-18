from array_builder import *
from img_map import *
from convoluter import *

def map_construct(amount,scale,float_,value_sigmoid):
    for i in range(amount):
        print("GENERATED",i)
        #perlins_l = perlins(random.randrange(2,10),float_=float_) #all of this needs to be added to the array builder`s methods
        value=value_sigmoid #maximum value to be sigmoided in

        map_array = map_maker(scale=scale,object=0)

        settings_l0 = [#*perlins_l,
        {"method":perlin_,"args":{"octaves":random.choice([2,3,5,10]),"seed":random.randint(1,100),"object":0,
        "bias":random.choice([0.2,0.1,0,-0.1,-0.2]),"float":float_}},
        {"method":perlin_,"args":{"octaves":random.choice([2,3,5]),"seed":random.randint(1,100),"object":1,
        "bias":random.choice([0.2,0.1,0,-0.1,-0.2]),"float":float_}},
        {"method":perlin_,"args":{"octaves":random.choice([3,5,10]),"seed":random.randint(1,100),"object":2,
        "bias":random.choice([0.2,0.1,0,-0.1,-0.2]),"float":float_}},
        {"method":perlin_,"args":{"octaves":random.choice([2,4,6]),"seed":random.randint(1,100),"object":3,
        "bias":random.choice([0.2,0.1,0,-0.1,-0.2]),"float":float_}},

            #{"method":bias_,"args":{"bias":-2,"values":(225,275)}},
            #{"method":sigmoid_,"args":{"num":value,"float":True}},
        ]
        
        settings_l1 = [*settings_l0,
        {"method":convert_float_to_int,"args":{"segments":4}},
        {"method":border,"args":{"bordersize":70,"object":4}}
        ]
        array1 = (array_builder(map_array,steps=settings_l1))
        save_map(array1,color_dict=None,draw=True,float=False,settings=settings_l1,value=value)

        settings_l2 = [*settings_l0,
        {"method":bias_,"args":{"bias":0.5}},
        #{"method":sigmoid_,"args":{"num":value,"float":True}},
        {"method":convert_float_to_int,"args":{"segments":4}},
        {"method":border,"args":{"bordersize":70,"object":4}}
        ]
        array2 = (array_builder(map_array,steps=settings_l2))
        save_map(array2,color_dict=None,draw=True,float=False,settings=settings_l2,value=value,extend="a")

        settings_l3 = [*settings_l0,
        {"method":bias_,"args":{"bias":1}},
        #{"method":sigmoid_,"args":{"num":value,"float":True}},
        {"method":convert_float_to_int,"args":{"segments":4}},
        {"method":border,"args":{"bordersize":70,"object":4}}
        ]
        array3 = (array_builder(map_array,steps=settings_l3))
        save_map(array3,color_dict=None,draw=True,float=False,settings=settings_l3,value=value,extend="b")

        settings_l4 = [*settings_l0,
        {"method":bias_,"args":{"bias":1.5}},
        #{"method":sigmoid_,"args":{"num":value,"float":True}},
        {"method":convert_float_to_int,"args":{"segments":4}},
        {"method":border,"args":{"bordersize":70,"object":4}}
        ]
        array4 = (array_builder(map_array,steps=settings_l4))
        save_map(array4,color_dict=None,draw=True,float=False,settings=settings_l4,value=value,extend="c")


        #map drawing needs a smear mode for floats where the average of the 
        #nearest two integers` rgb values are taken, 
        # so 1:(100,100,100). 2:(200:200:200) -> a float of 1.5 has the value 150,150,150

map_construct(amount = 10, scale = 15,float_=True,value_sigmoid=5)