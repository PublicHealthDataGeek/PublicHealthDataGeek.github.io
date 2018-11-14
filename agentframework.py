"""

"Sheep eating grass" - Agent (Sheep framework)

This program forms part of the Agent-Based Model that shows a field of sheep 
eating grass whilst communicating their position with the other members of 
their flock.  This pa rticular part of code creates an 'Class' of Sheep (Agents). 
It defines a number of their abilities using functions including moving, eating
and figuring out how far they are from other sheep. 


It was created as part of the Programming for Social Sciences Module at the 
University of Leeds in Autumn 2018
"""
#Import required modules
import random

# Create the Agent (sheep) class
class Agent:
    def __init__(self, environment, agents): 
        self._y = random.randint(0,99)  
        self._x = random.randint(0,99)
        self.environment = environment
        self.store = 0 
        self.agents = agents
        
    def move(self):
        """Function to move the agents"""
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

    def eat(self):
        """Function to get sheep to eat 10 units"""
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

    def distance_between (self, agent):
        """Function to calculate the distance between 2 sheep"""
        return(((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5

    def share_with_neighbours(self, neighbourhood):
        """Function to share food with the neighbouring sheep"""
        for agent in self.agents: 
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum / 2
                self.store = average
                agent.store = average
                return("Distance to nearest sheep: " + str(distance))
                
"""
The End
"""           
        