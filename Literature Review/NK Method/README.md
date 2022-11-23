# Quantum K-colouring with NK method

This is a more generalised approach to colour a graph with N-vertices with K-colours. Each node is given K qubits and a colouring matrix which is N x K is defined. So for a valid C, there should be one 1 and K-1 zeroes as each node can have only one colour. 

- Take the outer sum of the colouring matrix
- Concatenate the adjacency matrix of the graph K times
- Element wise product of the first two results

If we take the maximum from each row then it should be less than 2. That is, it should either be 0 or 1.

The superpositions of all colouring matrices will be k<sup>n</sup>.

The time complexity in terms of number of qubits is O(N<sup>2</sup>). In terms of n and k it would be O(k<sup>2n</sup>), where n is the number of vertices and k is the number of colours.
