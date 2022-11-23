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

def add_circuit_for_acc_and(qc,inter_ar,final_ar,out):

    qc.mct([inter_ar[1],inter_ar[0]],final_ar[0])

    for i in range(2,len(inter_ar)-1):
        qc.mct([final_ar[i-2],inter_ar[i]],final_ar[i-1])
    
    qc.mct([inter_ar[-1],final_ar[-1]],out)

def clean_ancilla_for_acc_and(qc,inter_ar,final_ar):

    for i in reversed(range(2,len(inter_ar)-1)):
        qc.mct([final_ar[i-2],inter_ar[i]],final_ar[i-1])
    
    qc.mct([inter_ar[1],inter_ar[0]],final_ar[0])


def generate_oracle(quantumCircuit,qr,inter_ar,final_ar,out,sat_repr,variables):

    # Map of index for each variable
    variables_to_qr_map = dict(zip(variables,[i for i in range(len(variables))]))

    # Superposition
    for i in range(len(variables)):
        quantumCircuit.h(qr[i])

    # Intermediate results
    for i in range(len(sat_repr)):
        add_circuit_for_clause(sat_repr[i],quantumCircuit,qr,inter_ar[i],variables_to_qr_map)

    # Doing an and of all the results
    add_circuit_for_acc_and(quantumCircuit,inter_ar,final_ar,out)

    # Cleaning up final and ancillae bits
    clean_ancilla_for_acc_and(quantumCircuit,inter_ar,final_ar)

    # Cleaning up inter ancillae bits
    for i in range(len(sat_repr)):
        clean_ancilla_for_clause(sat_repr[i],quantumCircuit,qr,inter_ar[i],variables_to_qr_map)

def generate_diffuser_circuit(quantumCircuit,qr,acc_ar,cr,out,variables):

    for i in range(len(variables)):
        quantumCircuit.h(qr[i])
        quantumCircuit.x(qr[i])

    quantumCircuit.x(out)
    quantumCircuit.h(out)
    
    # Accumulating and
    add_circuit_for_acc_and(quantumCircuit,qr,acc_ar,out)

    # Cleaning up ancillae
    clean_ancilla_for_acc_and(quantumCircuit,qr,acc_ar)

    quantumCircuit.h(out)
    quantumCircuit.x(out)
    quantumCircuit.h(out)

    for i in range(len(variables)):
        quantumCircuit.x(qr[i])
        quantumCircuit.h(qr[i])
        

def generate_quantum_circuit_for_sat(sat_repr,variables):

    # Number of qubits required
    num_qubits = len(variables)

    # Number of iterations
    num_iter = 2 ** int((len(variables)+1)/2)

    # Number of and gates required for intermediate ands
    num_inter_ancilla_bits = len(sat_repr)

    # Number of and gate required for final accumulation of results
    # To add N numbers we need N-1 gates, we already have one for out so N-2
    num_acc_ancilla_bits = len(sat_repr) - 2

    # Defining quantum circuit parameters
    qr = QuantumRegister(num_qubits)
    out = QuantumRegister(1)
    inter_ar = AncillaRegister(num_inter_ancilla_bits)
    acc_ar = AncillaRegister(num_acc_ancilla_bits)
    cr = ClassicalRegister(num_qubits)
    quantumCircuit = QuantumCircuit(qr,out,inter_ar,acc_ar,cr)

    num_iter = 9
    for i in range(num_iter):
        generate_oracle(quantumCircuit,qr,inter_ar,acc_ar,out,sat_repr,variables)
        generate_diffuser_circuit(quantumCircuit,qr,acc_ar,cr,out,variables)
    
    # Measuring the outcome
    for i in range(len(variables)):
        quantumCircuit.measure(qr[i],cr[i])

    # Saving circuit png
    # quantumCircuit.draw(output='mpl').savefig('output/sat-solving-circuit.png') # find a way to extend horizontally
    return quantumCircuit
