# Search Algorithm Visualizer (BFS, DFS, and A* Algorithms)

## Instruction

Create a program that implements 3 search algorithms. Given the graph below as an input (Note: input could be from the user or already define input in your program).

The graph in the figure below shows the state space of a hypothetical search problem. States are denoted by letters, and the cost of each action is indicated on the corresponding edge. Note that actions are not reversible, since the graph is oriented. The table next to the state space shows the value of some admissible heuristic function, considering G as the goal state (it is easy to verify that such a heuristic never overestimates the true, minimum path cost from any given state to the goal state G).

<img width="827" alt="Screen Shot 2022-07-09 at 6 02 00 AM" src="https://user-images.githubusercontent.com/106197019/178075799-8e1abbd1-356f-40ab-8ea3-45d5fe07d3b4.png">

Considering S as the initial state, solve the above search problem using:
- breadth-first search
- depth-first search
- A* search with the heuristic above

Note: The output should display the graph (initial or above graph) and the final path to achieve goal G.

##  Submission

<img width="827" alt="Screen Shot 2022-07-09 at 6 02 55 AM" src="https://user-images.githubusercontent.com/106197019/178075882-f1485f17-4dfd-460e-989e-2b8e2374689f.png">

Above is the output of the program. It visualizes the graph and its paths from the initial state to the goal state using Breadth-First Search, Depth-First Search, and A* Search algorithms.  Please keep in mind that the program considers alphabetical ordering when choosing to traverse among the corresponding states (e.g., among nodes A, B, and F, node A is selected.) The paths are also shown simultaneously in the plot where RED edges indicate the BFS path, BLUE edges indicate the DFS path, and YELLOW edges indicate the A* path.

You may view the file for full documentation.
