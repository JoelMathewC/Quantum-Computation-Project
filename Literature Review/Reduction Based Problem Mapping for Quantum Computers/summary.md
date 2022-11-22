# Reduction-Based Problem Mapping for Quantum Computing

Quantum Computing is not experiencing the same growth as Quantum Computers and the widely believed statement that programming quantum computers is hard is backed up by solid evidence. To overcome this hurdle, we are introduced to an end-to-end framework that takes advantage of reductions. It relies on the property that NP-Complete problems can be reduced to each other in polynomial time and therefore does not require quantum specific modeling and encoding techniques for various problems.

This can be implemented by choosing a particular problem S and transforming the general input in polynomial time and the computed output is converted back to the desired output for the original input. The unrestricted Boolean-SAT is choosen as the general problem which can be solved with the help of Grover's Quantum Search Algorithm.

The quantum search algorithm is setup in such a way to search in an unordered collection of N items. From a classical POV, we need to make N/2 computations on average to find the item we are looking for. But from a Quantum POV, we can take advantage of Superposition. Coupled with the Oracle function and Diffusion operator, we can leverage the Grover's Amplitude Amplification trick to search for the desired state inside the superposed state. Compared to classical search, there is a significant speed up. O(N) compared to O(sqrt(N)).

With the help of IBM's Qiskit module, the SAT problem for a quantum computer was implemented consisting of a SAT Quantum Circuit Generator, a problem parser and a back-end quantum processor provided by Qiskit.

It was then evaluated on the SAT problem and the 3-Coloring problem.