from qiskit import *

def not_and_3_elem(qc,qr1,qr2,qr3,ar):
    qc.x(qr1)
    qc.x(qr2)
    qc.x(qr3)
    qc.mct([qr1,qr2,qr3],ar)
    qc.x(qr1)
    qc.x(qr2)
    qc.x(qr3)
    qc.x(ar)

def reverse_not_and_3_elem(qc,qr1,qr2,qr3,ar):
    qc.x(ar)
    qc.x(qr1)
    qc.x(qr2)
    qc.x(qr3)
    qc.mct([qr1,qr2,qr3],ar)
    qc.x(qr1)
    qc.x(qr2)
    qc.x(qr3)

def not_of_and_result(qc,qr1,qr2,ar):
    qc.mct([qr1,qr2],ar)
    qc.x(ar)

def reverse_not_of_and_result(qc,qr1,qr2,ar):
    qc.x(ar)
    qc.mct([qr1,qr2],ar)

def add_circuit_for_clause(clause,qc,qr,inter_ar,variables_to_qr_map):
    
    if len(clause) == 3:
        not_and_3_elem(qc,qr[variables_to_qr_map[clause[0][1:]]],
                        qr[variables_to_qr_map[clause[1][1:]]],
                        qr[variables_to_qr_map[clause[2][1:]]],
                        inter_ar)
    else:
        not_of_and_result(qc,qr[variables_to_qr_map[clause[0]]],
                            qr[variables_to_qr_map[clause[1]]],
                            inter_ar)

def clean_ancilla_for_clause(clause,qc,qr,inter_ar,variables_to_qr_map):
    
    if len(clause) == 3:
        reverse_not_and_3_elem(qc,qr[variables_to_qr_map[clause[0][1:]]],
                        qr[variables_to_qr_map[clause[1][1:]]],
                        qr[variables_to_qr_map[clause[2][1:]]],
                        inter_ar)
    else:
        reverse_not_of_and_result(qc,qr[variables_to_qr_map[clause[0]]],
                                qr[variables_to_qr_map[clause[1]]],
                                inter_ar)

def generate_sat_quantum_circuit(sat_repr,variables):

    # Number of qubits required
    num_qubits = len(variables)

    # Number of and gates required for intermediate ands
    num_inter_and_ancilla_bits = len(sat_repr)

    # Map of index for each variable
    variables_to_qr_map = dict(zip(variables,[i for i in range(len(variables))]))

    # Defining quantum circuit parameters
    qr = QuantumRegister(num_qubits)
    out = AncillaRegister(1)
    inter_ar = AncillaRegister(num_inter_and_ancilla_bits)

    quantumCircuit = QuantumCircuit(qr,out,inter_ar)

    # Superposition
    for i in range(len(variables)):
        quantumCircuit.h(qr[i])

    # Intermediate results
    for i in range(len(sat_repr)):
        add_circuit_for_clause(sat_repr[i],quantumCircuit,qr,inter_ar[i],variables_to_qr_map)

    # Doing an and of all the results
    quantumCircuit.mct(inter_ar,out)

    # Cleaning up ancillae bits
    for i in range(len(sat_repr)):
        clean_ancilla_for_clause(sat_repr[i],quantumCircuit,qr,inter_ar[i],variables_to_qr_map)

    # Saving circuit png
    quantumCircuit.draw(output='mpl').savefig('oracle.png')
    return quantumCircuit