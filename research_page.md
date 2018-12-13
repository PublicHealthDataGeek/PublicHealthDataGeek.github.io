My current projects are associated with the modules I am doing in the Masters in Data Analytics and Society. 



## 1. Programming for the Social Sciences.  
Assessment 1 involved learning about and coding an Agent Based Model of a flock of sheep nibbling grass in a field. 

Assessment 2 required me to build a program that reads in some data, processes it in some way, displays the results and writse the results to file.  I utilised an example project - The Black Death. 



### Sheep eating grass
------------------

This simulation shows a flock of sheep eating grass in a field.  They eat, move and share the grass with other members of the flock.  The default parameters are 20 sheep that move and eat 40 times.  

#### Getting started
Download the following files into a directory:
 - [The Model](/docs/SheepABMFinal.py)
 - [The Sheep](/docs/agentframework.py)
 - [The Dataset](/docs/in.txt)

These are the model, agents (sheep) and the data file for the environment respectively.  Run 'SheepABMFinal.py' from the command line and the model should start to run.  
You can alter the number of sheep by changing the `num_of_agents` and alter how often they move and eat by changing the `num_of_iterations`.  

#### Built with
 Spyder 3.3.1 IDE running Python 3.7.0

#### Author
 Caroline Tait

#### License
 This project is licensed under the MIT License - see the [LICENSE](/docs/LICENSE) file for details.


### The Black Death
------------------
This program imports and reads data on average rats caught and population density.  An equation is used to calculate the average number of human deaths from the Black Death and its outputs are saved to file.  Images of the data are generated and displayed. A Graphical User Interface allows the user to alter the parameters of the equation.   

#### Getting started
Download the following files into a directory:
 - [The Rats Caught Datafile](/docs/deathsrats.txt)
 - [The Population Density Datafile](/docs/deathsparishes.txt)
 - [The Jupyter notebook](/docs/)

These are the datafiles and Jupyter notebook than enables you to run the program.  Open the Jupyter notebook and follow the instructions within it to run the code.  

Should you wish to run it from a Python file then please download this file:  

- [Python code](/docs/P4SSAss2Final.py)

#### Built with
 Spyder 3.3.1 IDE running Python 3.7.0 and Jupyter Notebook (python36).

#### Author
 Caroline Tait

#### License
 This project is licensed under the MIT License - see the [LICENSE](/docs/LICENSE) file for details.
