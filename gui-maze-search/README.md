# GUI Maze Search

## Instruction

- The (x, y) coordinates of each node are defined by the column and the row shown at the top and left of the maze, respectively. For example, node 13 has (x, y) coordinates (1, 5).
- Process neighbors in increasing order. For example, if processing the neighbors of node 13, first process 12, then 14, then 21.
- Use a priority queue for your frontier. Add tuples of (priority, node) to the frontier. For example, when performing other search such as Uniform Cost Search and processing node 13, add (15, 12) to the frontier, then (15, 14), then (15, 21), where 15 is the distance (or cost) to each node.
- When removing nodes from the frontier (or popping off the queue), break ties by taking the node that comes first lexicographically. For example, if deciding between (15, 12), (15, 14) and (15, 21) from above, choose (15, 12) first (because 12 < 14 < 21).
- A node is considered visited when it is removed from the frontier (or popped off the queue).
- You can only move horizontally and vertically (not diagonally).
- It takes 1 minute to explore a single node. The time to escape the maze will be the sum of all nodes explored, not just the length of the final path.
- All edges have cost 1.
- Make sure to implement this problem with a GUI.

![image](https://user-images.githubusercontent.com/106197019/178066246-ed295cc2-4e5a-46f1-a7a9-fac379f44dd0.png)



## Submission

The program begins to search the A Star path (from 0 to 61) as soon as the corresponding button is clicked. First, all the nodes that are explored upon the search are highlighted by the color light yellow. The actual A Star path is then shown by being highlighted with the brighter color yellow. The highlighted nodes are cleared right after the ‘clear’ button is clicked. This allows searching the A star path again.

<img width="827" alt="Screen Shot 2022-07-09 at 4 36 06 AM" src="https://user-images.githubusercontent.com/106197019/178066689-db12f93e-54c4-4f84-b096-3112f3e983ab.png">

<img width="827" alt="Screen Shot 2022-07-09 at 4 37 32 AM" src="https://user-images.githubusercontent.com/106197019/178066817-6e38e4a8-c27a-4639-96ad-3055cc20b58f.png">

<img width="827" alt="Screen Shot 2022-07-09 at 4 37 55 AM" src="https://user-images.githubusercontent.com/106197019/178066854-c76706dd-49e3-4dd3-9a32-ded90127ad0d.png">

<img width="827" alt="Screen Shot 2022-07-09 at 4 38 12 AM" src="https://user-images.githubusercontent.com/106197019/178066892-bfd4dc59-a8c6-4a29-b474-9a20f98563a4.png">

<img width="827" alt="Screen Shot 2022-07-09 at 4 38 34 AM" src="https://user-images.githubusercontent.com/106197019/178066924-8ede3fc8-6076-4744-90bc-a4ae2e733636.png">


Disclaimer: The A* Path program was provided, and I had only written the interface.
