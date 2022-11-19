# Maximal Clique Problem

## Shifting the current problem to a sufficient sub-problem
If the problem is an m-colouring decision problem, then we just need to check if the maximum clique of the graph is greater than 3. If it is greater than 3, then it cannot be coloured with just 3 colours.

## Clique and Maximal Clique
A clique is just a complete sub-graph of a given graph. Every node in a clique is directly connected to each other in the original graph. The maximal clique is a sub-graph that is complete and has the most number of nodes. <p></p>
**Ref:** We have learnt about bi-partite graphs in Discrete Structures ans we also know that if the maximal clique is more than 2 then it ceases to be a bi-partite graph. 

## Approaches
A recursive approach can be adopted to find the maximal clique number but this can be done in polynomial time O(V<sup>2</sup>), where V is the number of vertices.

| # | Title |
|---| ----- | 
|1|[Maximal Clique Problem - Yale Lecture](http://www.stat.yale.edu/~yw562/teaching/684/lec02.pdf) | 
|2|[Greedy Approach](https://iq.opengenus.org/greedy-approach-to-find-single-maximal-clique/) | 
|3|[Recursive Approach](https://www.geeksforgeeks.org/maximal-clique-problem-recursive-solution/) | 

## Maximum Clique vs Maximum Clique Decision Problem
In Maximum clique decision problem, given a k value we have to find if there is a clique with the number of nodes greater than k. This is an NP-complete problem. In the case of maximum clique problem, we just find the number of nodes in the largest clique possible in the graph.

