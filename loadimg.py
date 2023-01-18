import pygame
def load_images(name_list,k,directory=None):

    if directory!=None:
        directory = f"{directory}/"
    else:
        directory=""

    image_names_dict = {}
    image_map_dict = {}
    image_number = 0
    for index,image_name in enumerate(name_list):
        image_names_dict[index+k] = image_name
        img = pygame.image.load(f"{directory}{image_name}.png").convert_alpha()
        image_map_dict[index+k] = img
        image_number+=1


    return name_list, image_names_dict,image_map_dict,image_number