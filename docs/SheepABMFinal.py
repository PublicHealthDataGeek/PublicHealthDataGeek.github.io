"""

"Sheep eating grass"

This program is an Agent-Based Model that shows a field of sheep eating grass
whilst communicating their position with the other members of their flock.

It was created as part of the Programming for Social Sciences Module at the 
University of Leeds in Autumn 2018

"""


# Import relevent modules
import matplotlib.pyplot as plot  
import matplotlib.animation
import csv
import random
import agentframework

# Set the Model parameters
num_of_agents = 20  
num_of_iterations = 40
neighbourhood = 20

# Create the picture of the field 
fig = plot.figure(figsize=(7, 7), edgecolor = 'g', linewidth=10)
ax = fig.add_axes([0, 0, 1, 1])

# Create lists for the environment and agents (aka the sheep)
environment = [] 
agents = [] 	

# Import data to create the environment/field for the sheep
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []				
    for value in row:	              
        rowlist.append(value)		  
    environment.append(rowlist)     
f.close() 

# Create the agents (sheep)
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))  

#Create the relevent functions to start and stop the animation of the sheep
def start(frame_number):
    fig.clear()   
    random.shuffle(agents)
    for i in range(num_of_agents):      
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        plot.scatter(agents[i]._x, agents[i]._y, color = "white")
        print(agents[i]._x, agents[i]._y)
    plot.ylim(0, 100)
    plot.xlim(0, 100)
    plot.xlabel('x position')
    plot.ylabel('y position')
    plot.title('A flock of sheep munching grass in a field')
    plot.imshow(environment)

def stop(b = [0]):
    a = 0
    while (a < num_of_iterations):
        yield a
        a = a + 1

# Animate the sheep in the field 
animation = matplotlib.animation.FuncAnimation(fig, start, frames=stop, repeat=False)
plot.show()

# Save their final positions in a csv file
f2 = open('finalenvironment.csv', 'w', newline='')
writer = csv.writer(f2, delimiter=' ')
for row in environment:
        writer.writerow(row)
f2.close()

"""
The End
"""