# 3 colouring problem

## Different kinds of problems
Just listing these for knowledge's sake. The problem we will be focussing on is the *3-colouring decision problem*

### m-colouring decision problem or m-colouring problem
Given m colours find if the graph can be coloured with these colours. The m in our case is 3. This is NP complete.

### m-colouring optimization problem
Given a graph find the minimum number (m) of colours required to colour the graph

### All possible solution list
List all the ways in which a given graph can be coloured with the given colours. Backtracking can be used to solve this.

## Solving the 3-colouring decision problem using Backtracking
Time Complexity: O(3^n) where n is number of vertices

*Note: The BFS approach in GFG is wrong since it does not actually colour the graph using the minimum number of colours. And hence will give NOT colourable even for cases when it is colourable. The BFS approach is a case of Greedy Colouring*

### Small footnote
Words from the author of a 3-coluring-problem medium article

```
I’ve found that the field is so massive that attempts to catalog all important developments were abandoned many years ago. Hence, I will restrict this to a very small set of concepts that reflect my personal interests.
```

So it must be justified to go with any algorithm of the same magnitude as that of the fastest algorithm. (In our case hopefully backtracking)

### Interesting facts
1. Graph coloring is required for solving a wide range of practical problems. For example, there is a coloring algorithm embedded in most compilers for register allocation.

Reference [here](https://medium.com/@tajhmcdon/3-color-algorithm-2d2d43050bba)