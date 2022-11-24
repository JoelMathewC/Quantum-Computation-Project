from qiskit import *
import math

def not_and_3_elem(qc,qr1,qr2,qr3,ar):
    qc.x(qr1)
    qc.x(qr2)
    qc.x(qr3)
    qc.mct([qr1,qr2,qr3],ar)
    qc.x(qr1)
    qc.x(qr2)
    qc.x(qr3)

def not_of_and_result(qc,qr1,qr2,ar):
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
        not_and_3_elem(qc,qr[variables_to_qr_map[clause[0][1:]]],
                        qr[variables_to_qr_map[clause[1][1:]]],
                        qr[variables_to_qr_map[clause[2][1:]]],
                        inter_ar)
    else:
        not_of_and_result(qc,qr[variables_to_qr_map[clause[0]]],
                                qr[variables_to_qr_map[clause[1]]],
                                inter_ar)

def add_circuit_for_acc_and(qc,inter_ar,final_ar,out):

    final_ar_index = 0
    qc.mct([inter_ar[1],inter_ar[0]],final_ar[0])

    if len(final_ar) > 1:
        for i in range(2,len(inter_ar)-1):
            qc.mct([final_ar[i-2],inter_ar[i]],final_ar[i-1])
            final_ar_index = i-1
    
    qc.mct([inter_ar[-1],final_ar[final_ar_index]],out)

def clean_ancilla_for_acc_and(qc,inter_ar,final_ar):

    if len(final_ar) > 1:
        for i in reversed(range(2,len(inter_ar)-1)):
            qc.mct([final_ar[i-2],inter_ar[i]],final_ar[i-1])
    
    qc.mct([inter_ar[1],inter_ar[0]],final_ar[0])


def generate_oracle(quantumCircuit,qr,inter_ar,final_ar,out,sat_repr,variables):

    # Map of index for each variable
    variables_to_qr_map = dict(zip(variables,[i for i in range(len(variables))]))

    # Superposition
    for i in range(len(variables)):
        quantumCircuit.h(qr[i])
    
    for i in range(len(inter_ar)):
        quantumCircuit.x(inter_ar[i])
    
    # out register init
    # quantumCircuit.x(out)
    # quantumCircuit.h(out)

    # Intermediate results
    for i in range(len(sat_repr)):
        add_circuit_for_clause(sat_repr[i],quantumCircuit,qr,inter_ar[i],variables_to_qr_map)

    # Doing an and of all the results
    add_circuit_for_acc_and(quantumCircuit,inter_ar,final_ar,out)

    # Cleaning up final and ancillae bits
    clean_ancilla_for_acc_and(quantumCircuit,inter_ar,final_ar)

    # Cleaning up inter ancillae bits
    for i in reversed(range(len(sat_repr))):
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
        

def generate_quantum_circuit_for_sat(sat_repr,variables,num_colour):

    # Number of qubits required
    num_qubits = len(variables)

    # Number of iterations
    # TODO: Add the M factor
    # num_iter = 2 ** int((len(variables)+1)/2)
    # Setting it to max 3, for faster execution
    num_iter = 0
    if len(variables)/num_colour == 1:
        num_iter = 1
    else:
        num_iter = 3

    # Number of and gates required for intermediate ands
    num_inter_ancilla_bits = len(sat_repr)

    # Number of and gate required for final accumulation of results
    # To add N numbers we need N-1 gates, we already have one for out so N-2
    num_acc_ancilla_bits = len(sat_repr) - 2

    # Defining quantum circuit parameters
    qr = QuantumRegister(num_qubits)
    out = QuantumRegister(1)
    inter_ar = QuantumRegister(num_inter_ancilla_bits)
    acc_ar = QuantumRegister(num_acc_ancilla_bits)
    cr = ClassicalRegister(num_qubits)
    quantumCircuit = QuantumCircuit(qr,out,inter_ar,acc_ar,cr)

    for i in range(num_iter):
        generate_oracle(quantumCircuit,qr,inter_ar,acc_ar,out,sat_repr,variables)
        generate_diffuser_circuit(quantumCircuit,qr,acc_ar,cr,out,variables)
    
    # Measuring the outcome
    for i in range(len(variables)):
        quantumCircuit.measure(qr[i],cr[i])

    # Saving circuit png
    if len(variables) < 9:
        quantumCircuit.draw(output='mpl',fold=-1).savefig('output/sat-solving-circuit-{}Nodes.png'.format(len(variables)/num_colour))

    return quantumCircuit
