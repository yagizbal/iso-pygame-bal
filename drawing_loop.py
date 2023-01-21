import pygame
import numpy as np
import os 
import sys
from loadimg import *
from game_loop import *

pygame.init()

screen_x = 1200
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))    #set the display mode, window title and FPS clock
pygame.display.set_caption('screen')
FPSCLOCK = pygame.time.Clock()

ttf_path = os.path.join(sys.path[0], "manaspc.ttf")
the_gui_font = pygame.font.Font(ttf_path, 14)

tile_list, tile_names, tile_map, tiles_number = load_images(
    ["iso_water","iso_fertile","iso_grass","iso_desert","border"],0,"resources")
pop_list, pop_names, pop_map, pop_number = load_images(
    ["p0","pop","dog"],0,"resources")
entity_list, entity_names, entity_map, entity_number = load_images(
    ["iso_rocks","iso_tree","iso_banan","branches","broken rocks"],1,"resources")
list_of_dictionaries = [tile_map,pop_map,entity_map]

print("a",tile_map)

#gui_bottom = pygame.image.load("gui_bottom.png").convert_alpha()


speed = 1

display_tiles_x = 65
display_tiles_y = 65

tile_width = 64 
tile_height = 64
tile_height_half = tile_height /2
tile_width_half = tile_width /2
editor_mode = True

CURRENT_STATE = 0
switchu = {1:0,0:1}
btn_values = [[50,114],[50,562]]
guiwidth = [32,512]

SLC = ("tile",1)
visible = True
time = 0

camera_x = 65
camera_y = 65

while True:
    time +=0.1
    keys = pygame.key.get_pressed()

    for event in pygame.event.get(): #to quit
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()    
    
    if visible==True:
        if camera_x<70:
            camera_x = 70
        elif camera_x>grid[0]:
            camera_x = grid[0]
        if camera_y<70:
            camera_y = 70
        elif camera_y>grid[0]:
            camera_y = grid[0]
        
        screen.fill((0,0,0))
        gui_buttons_map = {}
        
        if (keys[pygame.K_RIGHT] and keys[pygame.K_UP]):
            camera_x -=speed
        elif (keys[pygame.K_LEFT] and keys[pygame.K_UP]):
            camera_y -=speed
        elif (keys[pygame.K_LEFT] and keys[pygame.K_DOWN]):
            camera_x +=speed
        elif (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]):
            camera_y +=speed        
        elif (keys[pygame.K_RIGHT]):
            camera_x -=speed
            camera_y +=speed
        elif (keys[pygame.K_LEFT]):
            camera_x +=speed
            camera_y -=speed
        elif (keys[pygame.K_DOWN]):
            camera_x+=speed
            camera_y+=speed
        elif (keys[pygame.K_UP]):
            camera_y-=speed
            camera_x-=speed

        map_visible = map_full[camera_y-display_tiles_y:camera_y,camera_x-display_tiles_x:camera_x]
        entity_visible = entity_full[camera_y-display_tiles_y:camera_y,camera_x-display_tiles_x:camera_x]
        pops_visible = np.zeros(map_visible.shape)

        for pop in pops_list:
            tmi = int(time)
            if (camera_y-display_tiles_y<pop.history[tmi][1]<camera_y) and (camera_x-display_tiles_x<pop.history[tmi][0]<camera_x):
                pops_visible[pop.history[tmi][1]-camera_y,pop.history[tmi][0]-camera_x]=pop.type_index
        list_of_visible_arrays = [map_visible,pops_visible,entity_visible]

        for y, row in enumerate(map_visible):
            for x, tile in enumerate(row):
                cartesian_x = y * tile_width_half
                cartesian_y = x * tile_height_half  
                isometric_x = (cartesian_x - cartesian_y) 
                isometric_y = (cartesian_x + cartesian_y)/2
                centered_x = screen.get_rect().centerx + isometric_x
                centered_y = screen.get_rect().centery/2 + isometric_y

                for index_of_list, list_itself in enumerate(list_of_visible_arrays): 
                    tile = int(list_itself[y][x])                
                    image = list_of_dictionaries[index_of_list].get(tile)

                    if index_of_list==0:
                        screen.blit(image, (centered_x, centered_y-screen_y))
                    elif tile!=0:
                        screen.blit(image, (centered_x, centered_y-screen_y))


        if pygame.mouse.get_pressed()[0]:
            clicked_x,clicked_y = pygame.mouse.get_pos()
            clicked_x=clicked_x
            clicked_y=clicked_y+screen_y
            text_surface2 = the_gui_font.render((f"Coordinates on screen (x,y): {clicked_x},{clicked_y-800}, camera (x,y): {camera_x},{camera_y}"), False, (33, 33, 33))
            screen.blit(text_surface2,(0,25))
                
            isometric_corrected_x = int(((2*clicked_y - clicked_x)*0.5)/32)+4
            isometric_corrected_y = int(((((2*clicked_y + clicked_x)*0.5)/32))-15)

            e_text=""
            p_text=""
                        
                    #if entity_visible[isometric_corrected_y][isometric_corrected_x]!=0:
                    #    e_text= f" It has a {entity_names.get(entity_visible[isometric_corrected_y][isometric_corrected_x])} on it."
                        
            tiletext= f" This tile is {tile_names.get(map_visible[isometric_corrected_y][isometric_corrected_x])}."

            text_surface = the_gui_font.render((f"You clicked (x:{isometric_corrected_x+camera_x-display_tiles_x}, y:{isometric_corrected_y+camera_y-display_tiles_y}).{tiletext}{e_text}{p_text}"), False, (33, 33, 33))
            screen.blit(text_surface,(0,0))

    FPSCLOCK.tick(60)
    pygame.display.flip()
    pygame.event.pump()

