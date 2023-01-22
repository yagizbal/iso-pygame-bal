from agent_script import *
import random
import os

pops_list = []

map_full = np.load(f'{os.getcwd()}/noise-generator/saved_arrays/601-b.npy',allow_pickle=True)
grid = map_full.shape
squares = grid[0]*grid[1]
print(grid)

def move(pop_,direction,map_full,entity_full=None):
    revert = [pop_.placement[0],pop_.placement[1]]        
    point_x = pop_.placement[0]-direction[0]
    point_y = pop_.placement[1]-direction[1]
    pop_.placement = [point_x,point_y]

    point_on_map = int(map_full[pop_.placement[1]][pop_.placement[0]])
    #point_on_entity = int(entity_full[pop_.placement[1]][pop_.placement[0]])
    #print(point_on_entity)
    if (point_on_map in [0,4]):# or (point_on_entity!=0):
        pop_.placement = revert
        pop_.energy-=10    

def create_pop(index,pops_number,map_array,pops_list):
    for i in range(pops_number):
        poppy = Agent(index,10000,[random.randint(65,map_array.shape[0]-65),random.randint(65,map_array.shape[1]-65)])
        pops_list.append(poppy)
    return pops_list

def create_entity_map(map_full,object,target,amounts,entity_full):
    if len(entity_full)==0:
        entity_full = np.zeros(map_full.shape)
    amounts1 = amounts
    a = np.where(map_full==target)
    for amount in range(len(a[0])):
        if random.random()<((1/squares)*amounts1*2) and amounts>1:
        #if np.random.randint((0,squares/len(a[0])))==1 and amounts>1:
            entity_full[a[0][amount]][a[1][amount]]=object
            amounts-=1
    print(amounts)
    return entity_full


#this function takes the coordinate of a population and returns a slice of the map around it
def get_map_slice(pop,map_full):
    x = pop.placement[0]
    y = pop.placement[1]
    map_slice = map_full[y-20:y+20,x-20:x+20]
    entity_slice = entity_full[y-20:y+20,x-20:x+20]
    return map_slice, entity_slice

def find_objects(map_slice,entity_slice,targetmap,target):
    maps = [map_slice,entity_slice]
    targetmap = maps[targetmap]
    a = np.where(targetmap==target)
    return a  

#this function finds a path to the object from find_objects
# it returns a list of coordinates to follow
# the obstacles are entity 1, map 0 and map 4
# the path is found by finding the shortest distance between the target and the population
#   
    
pops_list = create_pop(1,500,map_full,pops_list)
pops_list = create_pop(2,500,map_full,pops_list)

entity_full = create_entity_map(map_full=map_full,object=3,target=2,amounts=5000,entity_full=[])
entity_full = create_entity_map(map_full=map_full,object=2,target=2,amounts=5000,entity_full=entity_full)
entity_full = create_entity_map(map_full=map_full,object=1,target=2,amounts=2500,entity_full=entity_full)

entity_full = create_entity_map(map_full=map_full,object=2,target=1,amounts=10000,entity_full=entity_full)
entity_full = create_entity_map(map_full=map_full,object=3,target=1,amounts=10000,entity_full=entity_full)
entity_full = create_entity_map(map_full=map_full,object=1,target=1,amounts=2500,entity_full=entity_full)

entity_full = create_entity_map(map_full=map_full,object=3,target=3,amounts=2500,entity_full=entity_full)
entity_full = create_entity_map(map_full=map_full,object=2,target=3,amounts=2500,entity_full=entity_full)
entity_full = create_entity_map(map_full=map_full,object=1,target=3,amounts=2500,entity_full=entity_full)

final_time = 1000 #how many steps to run the game loop for
for time_t in range(final_time):
    
    for pop in pops_list:
        if random.random()<0.5:
            move(pop,random.choice([(0,1),(0,-1),(1,0),(-1,0)]),map_full)
        pop.history.append(pop.placement)

    #print(pops_list[0].placement)
