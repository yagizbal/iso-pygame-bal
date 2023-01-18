from PIL import Image, ImageDraw
import random
import numpy as np
import os

def draw_map(map_array,color_dict=None,float=False,value=1):
    if color_dict==None:
        color_dict = {0:(157,206,243),1:(105,119,46),2:(11,180,60),3:(244,211,86),4:(0,0,0)}
    
    if float==True:
        color_dict = {}
        for i in range(255):
            color_dict[i]=(i,i,i)
        map_array = np.rint((map_array*255)/value)

    if float==False:
        map_array = np.rint(map_array).astype(int)
    
    img = Image.new("RGB", (map_array.shape))
    img1 = ImageDraw.Draw(img)  
    img1.rectangle( [(0,0),(map_array.shape)] ,fill="white",outline="white")

    for element in color_dict:
        b,a = np.where(map_array==element)
        color = color_dict.get(element)
        for index,x in enumerate(a):
            y = b[index]
            img.putpixel((x,y),(color))
    
    return img


def save_map(map_array,color_dict=None,draw=True,float=False,flip=False,settings=False,value=1,extend=""):            
    already_saved = (os.listdir("saved_arrays"))
    a_ls = []
    for i in already_saved:
        l,b = i.split("-")
        a_ls.append(int(l))
    if len(a_ls)==0:
        a_ls.append(0)

    a_ls.sort()
    last_number = int(a_ls[-1])
    next_number = last_number+1

    generated_name = f"{next_number}-{extend}"
    if draw==True:
        img = draw_map(map_array,color_dict,float,value=value)        
        img.save(f"saved_images/{generated_name}.png")
        
        with open(f'{os.getcwd()}/saved_arrays/{generated_name}.npy', 'wb') as f:
            np.save(f, map_array)

        if settings!=False:
            with open(f'{os.getcwd()}/saved_settings/{generated_name}.txt', 'w') as f:
                f.write(str(settings))