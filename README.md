# 🥜 Quantum-Computation-Project

Course project for S7 Quantum Computing course in NITC.

## Problem Statement
The essence of problems where quantum computers fail to outperform classical computers

As of now, Quantum Computers cannot significantly outperform classical computers while trying to solve NP-complete problems. 

We narrowed down the problem statement by taking one such NP-complete problem to implement the solution for the same via both quantum and classical method. By doing so, we wished to analyse and conclude that there wasn't a notable improvement by implementing a quantum approach.

We chose the 3-colouring problem which is a flavour of the famous graph-colouring problem.

This repository documents our trials and tribulations in solving the given problem statement. As we realised that one of the main
challenges in this field is the lack of systematic documentation and
comprehensive code structuring, we have clearly documented our learning process. 

```console
│   .gitignore
│   README.md
│
├───assets
│       team-1.jpg
│       team-2.jpg
│       team-3.jpeg
│
├───Classical Approach
│       backtrack.py
│       README.md
│
├───Deliverables
│       Intro-Presentation.pdf
│       README.md
│
├───Learning Docs
│   │   README.md
│   │
│   ├───3-colouring-graph-notes
│   │       3-colouring-problem.md
│   │       3-colouring-quantum.md
│   │       grovers-algorithm.md
│   │       max-clique-problem.md
│   │
│   ├───assets
│   │       amplitude-amplification.png
│   │       grover-step1-result.png
│   │       grover-step1.png
│   │       grover-step2-result.png
│   │       grover-step2.png
│   │       grover-step3-result.png
│   │       grover-step3.png
│   │       grover-step4.png
│   │
│   ├───attempt-quantum
│   │       GraphColouring.ipynb
│   │       sat_to_qc.ipynb
│   │
│   └───learning-qiskit
│           first.ipynb
│
├───Literature Review
│   │   README.md
│   │   
│   ├───Chromatic Number Problem Approach
│   │       Exponential Time Quantum Algorithms for Graph Coloring.pdf
│   │       README.md
│   │
│   ├───NK Method
│   │       Quantum K-colouring NK method.pdf
│   │       README.md
│   │
│   ├───Older References
│   │       Max_Clique_Distributed.pdf
│   │       Performance_Comparison_For_Algos.pdf
│   │       Quantum_Algorithms_Maximum_Clique_Medium.pdf
│   │       Quantum_Colouring_Graphs.pdf
│   │       The_Limits_of_Quantum_Computers.pdf
│   │
│   └───Reduction Based Problem Mapping for Quantum Computers
│       │   README.md
│       │   Reduction-Based_Problem_Mapping_for_Quantum_Computing.pdf
│       │   summary.md
│       │   
│       └───images
│               diff op An.png
│               diffusion op formula.png
│               diffusion operator Mn.png
│               fig1.png
│               fig2a.png
│               fig2b.png
│               fig2c.png
│               grover_circuit_high_level.png
│               MCT.png
│               Mn.png
│
└───Quantum Approach
    │   graph.py
    │   main.py
    │   qiskit-backends.py
    │   quantumCircuit.py
    │   README.md
    │   
    ├───logs
    │       terminal.txt
    │
    ├───output
    │       circuit-output-1.jpg
    │       circuit-output-2.jpg
    │       circuit-output.jpg
    │       sat-solving-circuit.png
    │
    └───__pycache__
            graph.cpython-310.pyc
            quantumCircuit.cpython-310.pyc
```

## Team members
|S.L. No.| Name | Roll number | GitHub ID |
| ----- | -------- | -------- | -------- |
|1|Nithin Puthalath Manoj|B190645CS|[@nithinmanoj10](https://github.com/nithinmanoj10)|
|2|Joel Mathew Cherian|B190664CS|[@JoelMathewC](https://github.com/JoelMathewC)|
|3|Pavithra Rajan|B190632CS|[@Pavithra-Rajan](https://github.com/Pavithra-Rajan)|
|4|Adwaith Ram Kishore|B190808CS| [@Adwaith-RK](https://github.com/Adwaith-RK)|

## Meet the team
![image](assets/team-1.jpg)
