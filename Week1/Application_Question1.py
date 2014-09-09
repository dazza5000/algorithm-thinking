"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import simpleplot
import math

# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(20)


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



###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

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



def normalize_graph_distribution(distribution_graph):
    
    normalized_distribution = {}
    
    degree_sum = sum(distribution_graph.values())
    
    for key, value in distribution_graph.items():
        normalized_distribution[key] = (float(value) / degree_sum)
        
    
    return normalized_distribution



def build_plot(normalized_graph):
    """
    Build plot of the number of increments in mystery function
    """

    plot = []

    for key, value in normalized_graph.items():
    
        plot.append([math.log(key, 10), math.log(value, 10)])
        
    
    return plot

#print in_degree_distribution(EX_GRAPH1)
print in_degree_distribution(EX_GRAPH2)
print normalize_graph_distribution(in_degree_distribution(EX_GRAPH2))



citation_graph = load_graph(CITATION_URL)

degree_distribution = in_degree_distribution(citation_graph)

normalized_distribution = normalize_graph_distribution(degree_distribution)

print normalized_distribution

normalized_plot = build_plot(normalized_distribution)

print normalized_plot

simpleplot.plot_scatter("Iteration counts", 600, 600, "input", "counter", [normalized_plot])





