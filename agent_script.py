import numpy as np
import torch

class Agent:
    def __init__(self,type_index,energy_max,placement,age=None):
        self.type_index = type_index #holds the number of type which is used to access images and the list of lists 
        #of placement matrices
        self.energy_max = energy_max
        self.energy = energy_max
        self.history = []
        self.line_of_sight = 8
        self.placement = placement
        if age==None:
            self.age=7500
        self.lifespan = 30000
        self.history = [placement]

        self.movement_dict = [(0,1),(0,-1),(1,0),(-1,0)]
        self.mv = self.movement_dict[0]


        traits = [["speed","exploitation","aging_speed"],["movement_cost","exploration"]]

        genome = []
        length= len(traits[0])
        for i in range(length):
            genome.append(np.random.rand(1,5))
        self.genome = genome
