# Quantum Approach
This directory contains the source code of the quantum approach taken to solve the 3-colouring problem.

### Ensure that you are in the right directory
```console
pavithra@client:~/Desktop/Quantum-Computation-Project$ cd Quantum Approach
```

### Install all the required libraries
```console
pavithra@client:~/Desktop/Quantum-Computation-Project/Quantum Approach$ pip install -r requirements.txt
```
### To view the help menu
```console
pavithra@client:~/Desktop/Quantum-Computation-Project/Quantum Approach$ python3 main.py -h
```
```console
usage: main.py [-h] -f F

optional arguments:
  -h, --help  show this help message and exit
  -f F        Name of the file containing the adjacency matrix
```
### Run the python file
The desired adjacency matrix is passed as a CLI argument. It is stored in CSV format.
An example of one such CSV file for a graph with 3 nodes
```console
pavithra@client:~/Desktop/Quantum-Computation-Project/Quantum Approach$ cat input/nodes-3.csv
```
```console
0, 1, 1
1, 0, 1
1, 1, 0
```
The quantum circuit (if possible), histogram depicting the probability distribution of the valid colourings and coloured solutions for the given graph will be generated and stored in the location specified via the logs.

- This is the 3-colouring graph solution for a graph with **one node**. 

```console
pavithra@client:~/Desktop/Quantum-Computation-Project/Quantum Approach$ python3 main.py -f input/nodes-1.csv
```
```console
INFO 20:08:38: The adjacency matrix has been successfully read
INFO 20:08:38: Circuit has been created
INFO 20:08:38: Execution of simulator in progress
INFO 20:08:39: The possible solution graphs have been saved in output/graphs/1-nodes/coloured
INFO 20:08:39: Histogram has been plotted and saved in output/histograms/1-nodes.png
INFO 20:08:41: Quantum Circuit saved in output/circuits/sat-solving-circuit-1-Nodes.png
INFO 20:08:41: Time taken for execution: 2.890918731689453 sec
```

- This is the 3-colouring graph solution for a graph with **two nodes**. 
```console
pavithra@client:~/Desktop/Quantum-Computation-Project/Quantum Approach$ python3 main.py -f input/nodes-2.csv
```
```console
INFO 20:10:51: The adjacency matrix has been successfully read
INFO 20:10:52: Circuit has been created
INFO 20:10:53: Execution of simulator in progress
INFO 20:10:54: The possible solution graphs have been saved in output/graphs/2-nodes/coloured
INFO 20:10:54: Histogram has been plotted and saved in output/histograms/2-nodes.png
INFO 20:11:02: Quantum Circuit saved in output/circuits/sat-solving-circuit-2-Nodes.png
INFO 20:11:02: Time taken for execution: 10.211768388748169 sec
```
- This is the 3-colouring graph solution for a graph with **three nodes**. 
```console
pavithra@client:~/Desktop/Quantum-Computation-Project/Quantum Approach$ python3 main.py -f input/nodes-2.csv
```
```console
INFO 20:11:46: The adjacency matrix has been successfully read
INFO 20:11:46: Circuit has been created
INFO 20:13:31: Execution of simulator in progress
INFO 20:13:32: The possible solution graphs have been saved in output/graphs/3-nodes/coloured
INFO 20:13:33: Histogram has been plotted and saved in output/histograms/3-nodes.png
INFO 20:13:33: Time taken for execution: 107.15578389167786 sec
```
### The structure of this directory
```console
│   Design.drawio
│   graph.py
│   main.py
│   plot.py
│   qiskit-backends.py
│   quantumCircuit.py
│   README.md
│   requirements.txt
│
├───input
│       nodes-1.csv
│       nodes-2.csv
│       nodes-3.csv
│
├───logs
│       Sample.md
│
├───output
│   ├───circuits
│   │       sat-solving-circuit-1-Nodes.png
│   │       sat-solving-circuit-2-Nodes.png
│   │
│   ├───graphs
│   │   ├───1-nodes
│   │   │       coloured1.png
│   │   │       coloured2.png
│   │   │       coloured3.png
│   │   │       uncoloured.png
│   │   │
│   │   ├───2-nodes
│   │   │       coloured1.png
│   │   │       coloured2.png
│   │   │       coloured3.png
│   │   │       coloured4.png
│   │   │       coloured5.png
│   │   │       coloured6.png
│   │   │       uncoloured.png
│   │   │
│   │   └───3-nodes
│   │           coloured1.png
│   │           coloured2.png
│   │           coloured3.png
│   │           coloured4.png
│   │           coloured5.png
│   │           coloured6.png
│   │           uncoloured.png
│   │
│   └───histograms
│           1-nodes.png
│           2-nodes.png
│           3-nodes.png
│

```