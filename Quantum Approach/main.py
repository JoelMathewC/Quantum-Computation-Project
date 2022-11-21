from graph import Graph
from qiskit import *
from quantumCircuit import generate_quantum_circuit_for_sat
from qiskit.tools.visualization import plot_histogram

if __name__ == "__main__":

    # Adjacency Matrix
    graph_adj_matrix = [[0,1,1],
                        [1,0,1],
                        [1,1,0]]
    
    # Initialize graph object
    g = Graph()
    g.init_nodes_from_adj_matrix(graph_adj_matrix)

    # SAT represnetation for the graph
    sat_repr = g.graph_to_sat()

    # List of all variables in SAT (Hardcoded to solve 3-colour problem)
    variables = ["N1C{}".format(i) for i in range(1,4)]
    variables = variables + ["N2C{}".format(i) for i in range(1,4)]
    variables = variables + ["N3C{}".format(i) for i in range(1,4)]

    quantumCircuit = generate_quantum_circuit_for_sat(sat_repr,variables)
    print("Log: Circuit Creation Completed")

    # Quantum assembly simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Executing the simulator
    result = execute(quantumCircuit,backend=simulator).result()

    plot_histogram(result.get_counts(quantumCircuit))
