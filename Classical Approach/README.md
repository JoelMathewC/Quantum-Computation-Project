# Classical Approach
For various NP-complete problems, a brute force approach is observed to be the fastest classical algorithm. For some, a refined brute-force techniques like
backtracking can be adopted. Though the upper-bound time remains the same, the average time taken reduces.
Time complexity: O(3<sup>n</sup>), where n is the number of vertices
## Method:
- Assign colours to each vertex one by one
- Before each assignment, verify if any of the adjacent vertices have the same colour
- If there are no violations proceed else backtrack a step and reass