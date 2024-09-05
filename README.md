# Schelling Model

The Schelling model - the agent-based model to rule them all!

For more information on the Schelling model, google or read [(Schelling, 1969)](http://www.jstor.org/stable/1823701). It is an agent-based model, meaning that its intended interpretation is one of discrete interacting units. In a nutshell, every such unit in the Schelling model has a one of a finite number of types and a (relatively low) preference for homogeneity in their neighbourhood - for instance, they may want no more than 2/3 of their neighbourhood to be of other types. If this preference is not satisfied, the agent moves to a free location on the grid. A very robust finding from this family of models is that segregation by types can arise even in cases of relatively tolerant agents.

This project implements the Schelling model in a class-based manner, with the grid of the model being an instance of the Grid class and the agents all instances of the Agent class. Currently, it uses only two types of agents, 0 and 1, respectively.

# How to Use
Initialise the model with your desired parameters by storing `SchellingGrid(width, height, number_of_agents)` in a value. For instance, to create a Schelling model 15 cells across and 10 cells high with 60 agents called `my_model`, use `my_model = SchellingGrid(15, 10, 60)`. 

Populate the grid with agents by calling `my_model.populate()`.

To commence the simulation, use `my_model.tick(X)`, substituting the desired number for X. The programme will print the model in its initial state (before the simulation) and after X ticks.

# Plans
In the future, following features will be included:
* A more user-friendly visualisation for the simulation results
* Data analysis tools for simulation results

# REFERENCES

Schelling, T. C. (1969). Models of Segregation. The American Economic Review, 59(2), 488–493.