import random
import urllib2
import simpleplot
import math

# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(30)

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


def randomGraph(n,p):
   
    er_graph = {}
    
    for i in range(n):
        er_graph[i] = set([])      
    
    print er_graph
   
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if random.random() < p:
                    er_graph[i].add(j)
 

    return er_graph

def generate_dpa_graph(nodes, connections, initial_weight=1):
    """Return a random graph.
    New edges are chosen weighted according to previously-existing edges.

    nodes -- number of nodes
    connections -- number of connections for each node
    """
    from random import choice

    node_pool = []
    edges = 0
    graph = {}
    for node in range(nodes):
        graph[node] = set()
        for _ in range(connections):
            try:
                node2 = choice(node_pool)
            except IndexError:
                break  # first node, empty pool
            if node2 in graph[node]:
                # avoid book-keepping duplicate edges.
                continue
            graph[node].add(node2)
            node_pool.append(node2)
            edges += 1
        node_pool.extend([node]*initial_weight)

    print 'Created graph with', nodes, 'nodes and', edges, 'edges.'
    return graph


def generate_er_digraph(num_nodes, p):
    er_digraph = dict()
    for node in range(num_nodes):
        er_digraph[node] = set([])
    for node_i in range(num_nodes):
        for node_j in range(num_nodes):
            if node_i != node_j:
                a = random.random()
                if a < p:
                    er_digraph[node_i].add(node_j)
    return er_digraph


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
    
        plot.append([math.log(key), math.log(value)])
        
    
    return plot

citation_graph = generate_dpa_graph(27770, 13, initial_weight=5)

degree_distribution = in_degree_distribution(citation_graph)

normalized_distribution = normalize_graph_distribution(degree_distribution)

print normalized_distribution

normalized_plot = build_plot(normalized_distribution)

print normalized_plot

simpleplot.plot_scatter("Iteration counts", 600, 600, "input", "counter", [normalized_plot])

