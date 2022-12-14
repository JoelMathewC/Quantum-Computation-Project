# π₯ Quantum-Computation-Project

Course project for S7 Quantum Computing course in NITC.

## Problem Statement
The essence of problems where quantum computers fail to outperform classical computers

As of now, Quantum Computers cannot significantly outperform classical computers while trying to solve NP-complete problems. 

We narrowed down the problem statement by taking one such NP-complete problem to implement the solution for the same via both quantum and classical method. By doing so, we wished to analyse and conclude that there wasn't a notable improvement by implementing a quantum approach.

We chose the 3-colouring problem which is a flavour of the famous graph-colouring problem.

This repository documents our trials and tribulations in solving the given problem statement. As we realised that one of the main
challenges in this field is the lack of systematic documentation and
comprehensive code structuring, we have clearly documented our learning process. 

## Code
To view the details regarding the quantum approach to solve the 3-colouring graph problem, proceed to [Quantum Approach](https://github.com/JoelMathewC/Quantum-Computation-Project/tree/main/Quantum%20Approach) directory.
```console
β   README.md
β
ββββassets
β       team-1.jpg
β
ββββClassical Approach
β       backtrack.py
β       README.md
β
ββββDeliverables
β       Group04_Phase1_Abstract_Presentation.pdf
β       Group04_Phase2_Presentation.pdf
β       Group04_Phase3_Final_Report.pdf
β       README.md
β
ββββLearning Docs
β   β   README.md
β   β
β   ββββ3-colouring-graph-notes
β   β       3-colouring-problem.md
β   β       3-colouring-quantum.md
β   β       grovers-algorithm.md
β   β       max-clique-problem.md
β   β
β   ββββassets
β   β       amplitude-amplification.png
β   β       grover-step1-result.png
β   β       grover-step1.png
β   β       grover-step2-result.png
β   β       grover-step2.png
β   β       grover-step3-result.png
β   β       grover-step3.png
β   β       grover-step4.png
β   β
β   ββββattempt-quantum
β   β       GraphColouring.ipynb
β   β       sat_to_qc.ipynb
β   β
β   ββββlearning-qiskit
β           first.ipynb
β
ββββLiterature Review
β   β   README.md
β   β
β   ββββChromatic Number Problem Approach
β   β       Exponential Time Quantum Algorithms for Graph Coloring.pdf
β   β       README.md
β   β
β   ββββNK Method
β   β       Quantum K-colouring NK method.pdf
β   β       README.md
β   β
β   ββββOlder References
β   β       Max_Clique_Distributed.pdf
β   β       Performance_Comparison_For_Algos.pdf
β   β       Quantum_Algorithms_Maximum_Clique_Medium.pdf
β   β       Quantum_Colouring_Graphs.pdf
β   β       The_Limits_of_Quantum_Computers.pdf
β   β
β   ββββReduction Based Problem Mapping for Quantum Computers
β       β   README.md
β       β   Reduction-Based_Problem_Mapping_for_Quantum_Computing.pdf
β       β   summary.md
β       β
β       ββββimages
β               diff op An.png
β               diffusion op formula.png
β               diffusion operator Mn.png
β               fig1.png
β               fig2a.png
β               fig2b.png
β               fig2c.png
β               grover_circuit_high_level.png
β               MCT.png
β               Mn.png
β
ββββQuantum Approach
    β   Design.drawio
    β   graph.py
    β   main.py
    β   plot.py
    β   qiskit-backends.py
    β   quantumCircuit.py
    β   README.md
    β   requirements.txt
    β
    ββββinput
    β       nodes-1.csv
    β       nodes-2.csv
    β       nodes-3.csv
    β
    ββββlogs
    β       Sample.md
    β
    ββββoutput
    β   ββββcircuits
    β   β       sat-solving-circuit-1-Nodes.png
    β   β       sat-solving-circuit-2-Nodes.png
    β   β
    β   ββββgraphs
    β   β   ββββ1-nodes
    β   β   β       coloured1.png
    β   β   β       coloured2.png
    β   β   β       coloured3.png
    β   β   β       uncoloured.png
    β   β   β
    β   β   ββββ2-nodes
    β   β   β       coloured1.png
    β   β   β       coloured2.png
    β   β   β       coloured3.png
    β   β   β       coloured4.png
    β   β   β       coloured5.png
    β   β   β       coloured6.png
    β   β   β       uncoloured.png
    β   β   β
    β   β   ββββ3-nodes
    β   β           coloured1.png
    β   β           coloured2.png
    β   β           coloured3.png
    β   β           coloured4.png
    β   β           coloured5.png
    β   β           coloured6.png
    β   β           uncoloured.png
    β   β
    β   ββββhistograms
    β           1-nodes.png
    β           2-nodes.png
    β           3-nodes.png
    β
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
