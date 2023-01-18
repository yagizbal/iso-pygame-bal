import numpy as np
import os
from array_builder import *
from img_map import *

def load_array(draw=None):
    ls = (os.listdir("saved_arrays"))[1:]
    chosen = random.choice(ls)
    mappe = np.load(f'{os.getcwd()}/saved_arrays/{chosen}',allow_pickle=True)

    if draw==True:
        draw_map(mappe,color_dict=False,float=True).show()
    return mappe