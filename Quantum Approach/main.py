from graph import Graph
from qiskit import *
from quantumCircuit import generate_quantum_circuit_for_sat
from qiskit.tools.visualization import plot_histogram
import time

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

    print(result.get_counts(quantumCircuit))
    plot_histogram(result.get_counts(quantumCircuit),filename="output/circuit-output.jpg")
    print("Time takes for execution: {} sec".format(time.time() - start_time))