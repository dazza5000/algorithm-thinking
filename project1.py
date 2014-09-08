"""
Functions and variables required for 
Project 1 - Degree distributions for graphs 
"""

EX_GRAPH0 = {0: set([1,2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2, 6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}

#print EX_GRAPH0
#print EX_GRAPH1
#print EX_GRAPH2

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and 
    returns a dictionary corresponding to a 
    complete directed graph with the specified number 
    of nodes.
    """
    complete_graph = {}
    
    if num_nodes < 0:
        return complete_graph
    
    for dummy_x in range(num_nodes):
        complete_graph[dummy_x] = set([])
        for dummy_y in range(num_nodes):
            if dummy_y != dummy_x:
                complete_graph[dummy_x].add(dummy_y)
    
    
    return complete_graph

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) 
    and computes the in-degrees for the nodes in the graph.
    """
    degree_graph = {}
    for key, value in digraph.items():
        degree_graph[key] = 0
        for dummy_x in value:
            degree_graph[dummy_x] = 0
    for key, value in digraph.items():
        for dummy_x in value:
            degree_graph[dummy_x] += 1
            
    return degree_graph

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) 
    and computes the unnormalized distribution of the in-degrees of 
    the graph.
    """
    degree_distribution = {}
    
    degree_graph = compute_in_degrees(digraph)
    
    for key, dummy_value in degree_graph.items():
        degree_distribution[degree_graph[key]] = 0
    
    for key, dummy_value in degree_graph.items():
        degree_distribution[degree_graph[key]] += 1

    return degree_distribution           



#print compute_in_degrees(EX_GRAPH0)
#print compute_in_degrees(EX_GRAPH1)
print compute_in_degrees(EX_GRAPH2)


#print in_degree_distribution(EX_GRAPH0)
#print in_degree_distribution(EX_GRAPH1)
print in_degree_distribution(EX_GRAPH2)

                   


A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A

