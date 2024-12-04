# Graph represented using dictionary of dictionaries
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

# function 
def dfs_search_with_distance(graph, start, goal):
    stack = [(start, 0)]  # Stack holds a list containing start node and 0 ie the distance calculated
    visited = {} # dictionary to keep track of visited nodes
    came_from = {} # dictionary to keep track of parent node
    distances = {}  # dictionary to hold cumulative distance from start to each visited node
    
    visited[start] = True # start node marked as visited
    came_from[start] = None # parent will be none for the start node
    distances[start] = 0 # distance will we zero from start node to it self
    
    # loop will run as long as stack is not empty this stack acts as storage for the nodes yet to explore 
    while stack:
        current, current_distance = stack.pop()  # to pop last node and its distance from the stack
        
        # if the current node is equal to the goal then the path to that is reconstructed using came_from dictionary
        if current == goal: 
            path = []   # empty list created to store the path
            distance = current_distance  # the total distance to each the goal node is stored in this distance
            
            # this runs until the current node is equal to none (empty) (to calculate the distance)
            while current is not None: 
                path.append(current) # current node is added to the path list this build the path in reverse order (goal to root)
                current = came_from[current] # updates the current to the current back tracked node using came from dictionary
            path.reverse() # as path contain the path list from goal to start we use reverse method to reverse it to start to goal
            return path, distance  # returns path and distance to the goal
        
        # this is to iterate over all the neighbors of the current node(current)
        for neighbor, dist in graph[current].items():  # dist is the distance between current and neighbor
                                                     # in graph[current] keys are the neighbor of the current node
                                                     # values are the distances from the current to each neighbor
            
       
            if neighbor not in visited: # ensure only unvisited neighbors are visited
                visited[neighbor] = True # mark the neighbor visited
                came_from[neighbor] = current # updates came from to current
                new_distance = current_distance + dist # calculate the distance from current node to neighbor
                distances[neighbor] = new_distance # stores the new distance in the distances dictionary for the neighbor node
                stack.append((neighbor, new_distance)) # update the values in the stack
    
    return None, None

# Example usage
start = 'Arad'
goal = 'Bucharest'
path, distance = dfs_search_with_distance(graph, start, goal)
if path:
    print("Path from", start, "to", goal, ":", path)
    print("Total distance:", distance)
else:
    print("No path found from", start, "to", goal)


#  This systematic approach guarantees that each node is visited exactly once, and nodes are explored
#  in depth-first order based on the stack's Last-In-First-Out (LIFO) structure.