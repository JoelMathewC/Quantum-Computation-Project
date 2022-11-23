# Literature Review
This directory contains all the papers that we have reviewed for the execution of this project.
```console
├───Chromatic Number Problem Approach
├───NK Method
├───Older References
└───Reduction Based Problem Mapping for Quantum Computers
```
The 3 colouring problem can be solved via a quantum method by converting it to an equivalent problem that yield the same result.
- ```Chromatic Number Problem Approach```: Compute the chromatic number and utilise Grover’s search
- ```NK method```: generation of superpositions of all possibilities and filtering
- ```Reduction Based Problem Mapping for Quantum Computers```: Reducing the problem to a SAT problem

We take the third approach because we know that by Cook's theorem, any NP problem can be reduced to SAT. We do not have a clear picture yet on how to encode data structures like graphs into quantum computers. SAT is well-studied and it closely relates to Boolean logic. By adding quantum search to the pipeline, any input problem that is reduces to SAT for which we use a quantum search can be transformed back to the original input.

```Older References``` contain all the papers that we had gone through to understand the problem statement better and narrow the scope down to what we have at the moment.