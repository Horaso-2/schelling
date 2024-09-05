import random
class SchellingGrid():
    # Initialise model with dimensions and number of agents
    def __init__(self, grid_width, grid_height, N):
        self.width = grid_width
        self.height = grid_height
        self.N = N
        self.create_grid()
        
    def __str__(self):
        output = ''
        for y in range(self.height):
            # Replace empty spaces on the grid with *'s. This is for visualisation only; in the script, empty spaces are stored as empty strings 
            line = ['*' if not self.grid[y][x] else repr(self.grid[y][x]) for x in range(self.width)]
            output += str(line) + '\n'
        return output
            
    def create_grid(self):
        self.grid = []
        for y in range(self.height):
            self.grid.append([])
            for x in range(self.width):
                self.grid[y].append('')
        
    def populate(self):
        self.agents = []
        empty_cells = self.get_empty_cells()
        for i in range(self.N):
            agent = SchellingAgent(i+1, 1/3, self)
            self.agents.append(agent)
            cell = random.choice(empty_cells)
            agent.position = cell
            self.grid[cell[1]][cell[0]] = agent
            empty_cells.remove(cell)
              
    def get_empty_cells(self):
        empty_cells = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '': 
                    empty_cells.append((x,y))
        return empty_cells
                
            
    def move_agent(self, agent):
        old_pos, new_pos = agent.position, random.choice(self.get_empty_cells())
        agent.position = new_pos
        self.grid[old_pos[1]][old_pos[0]] = ''
        self.grid[new_pos[1]][new_pos[0]] = agent
        
    def tick(self, ticks):
        print(f'Initial state:\n{model}')
        for _ in range(ticks):
            for agent in self.agents:
                agent.move()
        print(f'Final state after {ticks} ticks:\n{model}')
        
        

class SchellingAgent():
    # preference is the proportion of other-typed agents the agent can tolerate in the neighbourhood before requesting to move
    def __init__(self, id, preference, model):
        types = [0, 1]
        self.model = model
        self.id = id
        self.pref = preference 
        self.type = random.choice(types)
        self.parent_grid = model.grid
        self.position = (0, 0)

    def __str__(self):
        return f'ID: {self.id}, Type: {self.type}'
    
    def __repr__(self):
        return f'{self.type}'
    
    def get_neighborhood(self):
        cell_neighb = {}
        # Moore neighbourhood is used: 8 cells around the agent
        for y in range(max(self.position[1] - 1, 0), min(self.position[1] + 2, self.model.height)):
            for x in range(max(self.position[0] - 1, 0), min(self.position[0] + 2, self.model.width)):
                if self.model.grid[y][x]:
                    cell_neighb[(x,y)] = self.model.grid[y][x].type
                else: 
                    cell_neighb[(x,y)] = ''
                    
        # Remove agent's own position from their neighbourhood
        del cell_neighb[self.position]
        return cell_neighb
    
    # Calculate the proportion of other-typed agents in the neighborhood
    def get_concentration(self):
        neighb = self.get_neighborhood()
        '''
        I EMPLOY NEGATIVE PREFERENCE IN THIS MODEL: THE AGENT MOVES 
        IFF THERE'S MORE OF OPPOSITE TYPE RATHER THAN TOO FEW OF AGENT'S OWN TYPE
        '''
        my_types = [type for type in list(neighb.values()) if type == self.type]
        concentration = float(len(my_types)/len(neighb))
        return concentration
    
    def move(self):
        conc = self.get_concentration()
        # If too many of other-typed in the neighbourhood, the agent calls on the model to be moved
        if conc < self.pref:
            self.model.move_agent(self)
        

'''
EXAMPLE OF USAGE:

To initialise a 10x10 model with 60 agents and display it after 50 rounds:

model = SchellingGrid(10, 10, 60)
model.populate()
model.tick(50)
print(model)
'''




        


        
        