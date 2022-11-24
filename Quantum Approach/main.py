from graph import Graph
from qiskit import *
from quantumCircuit import generate_quantum_circuit_for_sat
from qiskit.tools.visualization import plot_histogram
import time
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def convert_result_percent(result, total):
    for k in result.keys():
        result[k] = result[k]/total
    return result

def set_threshold(num_node):
    if num_node == 3:
        return 0.015
    elif num_node == 2:
        return 0.1
    else:
        return 0   

def create_graph_from_adj(adjacency_matrix):
    G = nx.Graph(adjacency_matrix, nodetype=int)
    #print(G.edges())
    edges = G.edges()
    '''
    bidir_edges = []
    for i in edges:
        if (i[1], i[0]) not in bidir_edges:
            bidir_edges.append(i)
    print(bidir_edges)
    '''
    G.add_edges_from(edges)
    nx.draw(G, node_size=500, with_labels = True)
    plt.savefig("output/graphs/uncoloured2.png")
    return edges

def colour_graph(edges, colours, possibility_number, num_nodes):
    
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, scale=5)
    plt.figure()

    #graph = nx.draw_networkx(G,pos, node_color=color_map) 
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
    node_size=400, node_color=colours, alpha=0.9,
    labels={node: node for node in G.nodes()})

    plt.savefig("output/graphs/" + str(num_nodes) + "-nodes/coloured" + str(possibility_number) + ".png")

def split_possibility(result, num_qubits):
    #return [result[:3], result[3:6], result[6:]]
    i = 0
    states = []
    while (i < len(result)):
        states.append(result[i:i+num_qubits])
        i +=  num_qubits
    return states

if __name__ == "__main__":
    start_time = time.time()

    # Adjacency Matrix
    '''
        (N=1)   graph_adj_matrix = [[0]]
        (N=2)   graph_adj_matrix = [[0,1],
                                    [1,0]]
        (N=3)   graph_adj_matrix = [[0,1,1],
                                    [1,0,1],
                                    [1,1,0]]
    '''
    graph_adj_matrix = [[0,1,1],
                        [1,0,1],
                        [1,1,0]]

    # Number of colours
    num_colour = 3
    
    # Initialize graph object
    g = Graph()
    g.init_nodes_from_adj_matrix(graph_adj_matrix)

    # SAT represnetation for the graph
    sat_repr = g.graph_to_sat()
    # print("\n")
    # print("SAT REPR")
    # print(sat_repr)
    # print("\n")

    # List of all variables in SAT
    variables = []
    for i in range(len(graph_adj_matrix)):
        for j in range(num_colour):
            variables.append("N{}C{}".format(i+1,j+1))

    quantumCircuit = generate_quantum_circuit_for_sat(sat_repr,variables,num_colour)
    print("Log: Circuit Creation Completed")

    # Quantum assembly simulator
    simulator = Aer.get_backend('aer_simulator_matrix_product_state')

    # Executing the simulator
    result = execute(quantumCircuit,backend=simulator).result()

    #print(result.get_counts(quantumCircuit))
    sorted_result = dict(sorted(result.get_counts(quantumCircuit).items(), key=lambda x:x[1], reverse = True))
    #print(f"first {list(sorted_result.keys())[0]}")
    #print(sum(list(sorted_result.values())))
    #print(convert_result_percent(sorted_result, sum(list(sorted_result.values()))))
    percent_result = convert_result_percent(sorted_result, sum(list(sorted_result.values())))
    threshold = set_threshold(len(graph_adj_matrix))
    filtered_result = dict(filter(lambda elem: elem[1] > threshold, percent_result.items()))
    print(filtered_result)

    edges = create_graph_from_adj(np.array(graph_adj_matrix))
    colours = ['red', 'green', 'blue']
   
    all_colours = []

    for k in filtered_result.keys():
        states = split_possibility(k,3)
        #print(states)
        colours = []

        for s in states: 
            if s == '100':
                colours.append('red')
            elif s == '010':
                colours.append('green')
            else:
                colours.append('blue')
        all_colours.append(colours)
    #print(all_colours)
    
    possibility_number = 1
    for colours in all_colours:
        colour_graph(edges, colours, possibility_number, len(graph_adj_matrix))
        possibility_number += 1
    
    plot_histogram(filtered_result,filename="output/histograms/" + str(len(graph_adj_matrix)) + "-nodes" + ".png")
  
    print("Time taken for execution: {} sec".format(time.time() - start_time))