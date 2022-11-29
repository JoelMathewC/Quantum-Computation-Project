from graph import Graph
from qiskit import *
from quantumCircuit import generate_quantum_circuit_for_sat, draw_quantum_circuit
from qiskit.tools.visualization import plot_histogram
import time
import numpy as np
import csv
import argparse
from datetime import datetime
from plot import convert_result_percent, set_threshold, create_graph_from_adj, colour_graph, split_possibility

def log_time():
    return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, required=True, help="Name of the file containing the adjacency matrix")
    args = parser.parse_args()

    filename = args.f
    graph_adj_matrix = []
    with open(filename,'r') as data:
        for adj in csv.reader(data):
            graph_adj_matrix.append([int(node) for node in adj])
    print(f'INFO {log_time()}: The adjacency matrix has been successfully read')
    #print(graph_adj_matrix)

    edges = create_graph_from_adj(np.array(graph_adj_matrix))
    # Number of colours
    num_colour = 3
    
    # Initialize graph object
    g = Graph()
    g.init_nodes_from_adj_matrix(graph_adj_matrix)

    # SAT representation for the graph
    sat_repr = g.graph_to_sat()

    # List of all variables in SAT
    variables = []
    for i in range(len(graph_adj_matrix)):
        for j in range(num_colour):
            variables.append("N{}C{}".format(i+1,j+1))

    quantumCircuit, variables = generate_quantum_circuit_for_sat(sat_repr,variables,num_colour)
    print(f'INFO {log_time()}: Circuit has been created')
    
    # Quantum assembly simulator
    simulator = Aer.get_backend('aer_simulator_matrix_product_state')

    # Executing the simulator
    result = execute(quantumCircuit,backend=simulator).result()
    print(f'INFO {log_time()}: Execution of simulator in progress')

    #print(result.get_counts(quantumCircuit))
    sorted_result = dict(sorted(result.get_counts(quantumCircuit).items(), key=lambda x:x[1], reverse = True))
    #print(f"first {list(sorted_result.keys())[0]}")
    #print(sum(list(sorted_result.values())))
    #print(convert_result_percent(sorted_result, sum(list(sorted_result.values()))))
    percent_result = convert_result_percent(sorted_result, sum(list(sorted_result.values())))
    threshold = set_threshold(len(graph_adj_matrix))
    filtered_result = dict(filter(lambda elem: elem[1] > threshold, percent_result.items()))
    #print(filtered_result)

    #edges = create_graph_from_adj(np.array(graph_adj_matrix))
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
        file_path = colour_graph(edges, colours, possibility_number, len(graph_adj_matrix))
        possibility_number += 1
    print(f'INFO {log_time()}: The possible solution graphs have been saved in {file_path}')

    file_path = "output/histograms/" + str(len(graph_adj_matrix)) + "-nodes" + ".png"
    plot_histogram(filtered_result, filename = file_path)
    print(f'INFO {log_time()}: Histogram has been plotted and saved in {file_path}')
    file_path = draw_quantum_circuit(quantumCircuit, variables)
    if file_path!=None:
        print(f'INFO {log_time()}: Quantum Circuit saved in {file_path}')
    
    print(f'INFO {log_time()}: Time taken for execution: {time.time() - start_time} sec')


