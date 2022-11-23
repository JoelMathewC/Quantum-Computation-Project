# Exponential-Time Quantum Algorithms for Graph Coloring Problems
At present, the fastest known classical approach to decide the k-colourability of an N-vertex graph is still a exponential. In this literature, the quantum algorithm can compute the chromatic number with a time complexity **O(1.9140<sup>n</sup>)**.
Though the classical approach takes  **$\Omega$(2<sup>n</sup>)**, the quantum approach doesn't give a significant boost in performance. <p></p>

This approach uses **Byskov's algorithm** to compute the Maximal Independent Sets(MIS) of a fixed size. In graph theory, **MIS problem** revolves around finding the largest independent set in a graph. A set is independent if there is a set of vertices such that two vertices are not adjacent to each other. The backtracking method to find MIS is **O(2<sup>n</sup>)**. <p></p>

This method uses dynamic programming along with Grover's search on the MISs created by Byskov's algorithm. As the generation of MIS via Byskov's algorithm is a Branch and Reduce algorithm, we can apply Grover's search. A branching algorithm is an algorithm which recursively reduce a problem into problems with smaller parameters.

Enumerating all MISs will take a running time of O(3<sup>n/3</sup>) but if we apply Grover's search on it then it will take O(3<sup>n/6</sup>).

> For majority of NP-complete problems, an exhaustive search or a brute-force approach would be the fastest classical method. 

For some of these NP-complete problems, we can utilise refined approaches like backtracking. This just reduces the average time required but the worst-case or upper bound complexity ceases to decrease. 

As brute-force methods involve exhaustive searches, the running time can be quadratically improved via Grover's quantum search.

> QRAM analogous to RAM of a classical computer is criticised due to the difficulty in implementation. 

Other classical methods and complexities:
- Enumeration of all MIS and checking bipartiteness of the complement of MISs: **O(1.4423<sup>n</sup>)** (Eugene Lawler)
- Simple dynamic programming for chromatic number computation: **O(2.4423<sup>n</sup>)** (Eugene Lawler)
- An efficient algorithm suggested by Beigel and Eppstein with time complexity **O(1.3289<sup>n</sup>).** 

We change the k colouring to a k<sup>'</sup> colouring problem.
If we take a subset of vertices S such that the graph with those S vertices it is $\lfloor k/2 \rfloor$ colourable and the remaing graph excluding S is $\lceil k/2 \rceil$ colourable, then it is k-colourable.

## Chromatic number problem

If we have an MIS 'I' of size t and we choose T which is a subset of S excluding the nodes in MIS which satisfies |T| < |S|/2 and |S - I - T| is <= |S|/2 then it implies that |S|/2 - t <= |T| <= |S|/2. This is a sufficient condition to indicate that the chromatic number of the graph is correct. The complexity is **O(1.9140<sup>n</sup>)**



