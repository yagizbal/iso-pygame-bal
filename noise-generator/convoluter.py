import numpy as np
from img_map import *

#a=np.random.rand(250,250)
#print(a)
#a[0:20,0:20]=1

def convolute(array,kernel,stride):
    rows = array.shape[0]
    columns = array.shape[1]

    ls = []
    for row in range(rows-kernel):
        ls1=[]
        for i in range(columns-kernel):
            tile_value=np.sum(array[0+(row*stride):kernel+(row*stride),0+(i*stride):kernel+(stride*i)])/(kernel*kernel)
            ls1.append(tile_value)
        ls.append(ls1)
    ls=np.array(ls)
    return ls

#array,ls=convolute(a,3,1)
#img=draw_map(array,color_dict=False,float=True)
#img.show()


#img1=draw_map(ls,color_dict=False,float=True)
#img1.show()