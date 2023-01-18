import numpy as np
import random
from perlin_noise import PerlinNoise

def map_maker(scale,object):
    return np.full((100*scale,100*scale),object)

def array_builder(map_array, steps):
    temp_array = map_array
    for step in steps:
        temp_array=step["method"](temp_array,**step["args"])
    return temp_array

def sigmoid_(array,num,float=True):
    return num / (1+np.exp(-array))

def bias_(array,bias,values=None):
    if values==None:
        return array+bias
    else:
        array[values[0]:values[1]]+bias
        return array

def random_(array,probability,float=False):
    x = array
    for row in x:
        coords = np.random.randint(0,len(row),size=(int(len(row)*probability)))
        r = np.random.rand(*row.shape)
        row[coords] = r[coords]
        #print(row)
    return x

def perlins(howmany,float_):
    u = []
    for i in range(howmany):
        octave_random = random.choice([1,3,7,15])
        seed_random = random.randint(0,100)
        object_random = random.choice([0,1,2])
        bias_random = random.choice([0.15,0.1,0,-0.1,-0.2,-0.3,-0.4,-0.5])
        float_ = float_
        
        u.append({"method":perlin_,"args":{"octaves":octave_random,"seed":seed_random,"object":object_random,
        "bias":bias_random,"float":float_}})
    return u

def perlin_(array,octaves,seed,object,bias=0,float=False):
    grid = array.shape
    perlin = PerlinNoise(octaves=octaves, seed=seed)
    temp = ([[perlin([_/grid[0], __/grid[1]]) for __ in range(grid[0])] for _ in range(grid[1])])
    temp = np.array(temp)+bias
    
    if float==False:
        temp = (np.rint(sigmoid_(temp))).astype(int)
        temp_w = np.where(temp==1)
        for x in range(len(temp_w[0])):
            array[temp_w[0][x]][temp_w[1][x]] = object
    else:
        array = array+temp
    return array

def flip(map_array):
    zeroeth = np.flip(map_array,0)
    oneth = np.flip(map_array,1)
    z_one = np.flip(zeroeth,1)

    return map_array, zeroeth, oneth, z_one

def convert_float_to_int(array,segments):
    array= np.rint(array*(segments-1))
    array[array>segments-1]=segments-1
    array[array<0]=0
    return array

def convert_float_to_int_old(array,segments):
    max=np.max(array)
    min=np.min(array)
    
    #print("max",max)
    #print("min",min)

    difference=max-min #60
    step = difference/segments #25
    
    #[60,65,130,150,9999999,999999999]
    for i in range(len(segments)-1):
        array[array>segments[i]]=i-1
    return array



def border(map_array,bordersize,object):
    grid = map_array.shape
    x = grid[0]+bordersize
    y = grid[1]+bordersize
    border = np.full((x,y),object)
    border[35:-35,35:-35] = map_array
    map_array = border
    return map_array