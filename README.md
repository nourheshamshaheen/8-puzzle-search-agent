# 8-puzzle-search-agent
An artificial intelligence program using uninformed search and informed search to solve the 8-puzzle game.

## Intro
The goal of the 8-puzzle game is to find a sequence of moves that transitions an arbitrary initial state to the goal state.
This implementation is user-friendly as it shows the user the path to the goal represented on a 3x3 board using a GUI window and arrows to navigate between the states. 
For the GUI, I used a Qt-designed UI (mainwindow.ui), PyQt documentation and the PySide2 library. 

_Note: Not all initial states are solvable. An initial state is solvable if and only if it has an even number of inversions (without considering the blank tile)._

## Implementation

### Classes: 
-	State.py
-	Puzzle.py
-	Game.py
-	main.py

#### State.py
 This class defines each state as a “node”, having a cost, a parent, an array of values (order of numbers), a heuristic type (whether Manhattan, Euclidean or none for uninformed search) and a value for the heuristic function.
get_children(): This function swaps the “0” element with all possible adjacent elements to get the children of a certain node.
#### Puzzle.py
 This class defines the search algorithms used to find the solution:
 
**BFS():** This function utilizes the Breadth-First Search algorithm. It utilizes the deque library to implement a FIFO queue data structure using its popleft() and append() functions.
It also uses a list of arrays for previously visited or “explored” board states.

**DFS():** This function utilizes the Depth-First Search algorithm. It utilizes the deque library to implement a LIFO stack data structure using its pop() and append() functions.
It also uses a list of arrays for previously visited or “explored” board states.

_Note: The reason the “explored” set is made up of arrays and not nodes or states, is because many different nodes can have the same array values. That is, we can reach the same state from different path. However, in the actual implementation, these will technically be two different states (although, they have the same order of values in their arrays)._

**A_star():** This function has an input Type to specify whether the user wants the algorithm to consider the Manhattan distance or the Euclidean distance as the heuristic. It utilizes the A* algorithm. As well, it utilizes the heapq class to implement a priority queue data structure. 
#### Game.py
This class is to connect the GUI with the Puzzle class. It’s mainly a utility class so that the buttons can work, and the states can be displayed.
main.py
Driver class loading the UI file and executing the application.

***
