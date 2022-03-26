# 8-puzzle-search-agent
An artificial intelligence program using uninformed search and informed search to solve the 8-puzzle game.

## Intro
The goal of the 8-puzzle game is to find a sequence of moves that transitions an arbitrary
initial state to the goal state.
This implementation is user-friendly as it shows the user the path to the goal represented
on a 3x3 board using a GUI window and arrows to navigate between the states.

For the GUI, I used a Qt-designed UI (mainwindow.ui), PyQt documentation and the
PySide2 library.

Note: Not all initial states are solvable. An initial state is solvable if and only if it has an
even number of inversions (without considering the blank tile).
This program will tell you if an instance isn’t solvable using this concept and won’t run.
However, even without the “isSolvable” function, all of the algorithms will stop running
once the frontier list is empty and will print that the initial state is unsolvable.


## Implementation: Representation & Data Structures:

**States**: States are represented as a hashable python string.

**Explored:** Explored set is represented as a python set since it doesn’t allow duplicates and
searching in a set has an average time complexity O(1) and a worst case complexity O(n).

**Frontier list:**
*- In BFS:* FIFO Queue (using deque library)
*- In DFS:* LIFO Stack (using deque library)
*- In A*:* Priority Queue of tuples/ Min Heap (using heapq library)

**Parent map:** The parent map is a python dictionary (which is a hashmap).

**Cost map:** The cost map is also a python dictionary.

## Implementation: Classes:
 - Puzzle.py
 - Game.py
 - main.py

### Puzzle.py
This class defines the search algorithms used to find the solution – Notable funcions:

**BFS():** This function utilizes the Breadth-First Search algorithm. It utilizes the deque
library to implement a FIFO queue data structure using its popleft() and append()
functions. It also uses a set of strings for previously visited or “explored” board states. It
uses a hash map to store parent-child relationships.
       *
**DFS():** This function utilizes the Depth-First Search algorithm. It utilizes the deque library
to implement a LIFO stack data structure using its pop() and append() functions.
It also uses a set of strings for previously visited or “explored” board states. It uses a hash
map to store parent-child relationships.
       *
**A_star_man()/A_star_euc():** Both functions utilize the A* algorithm while using
Manhattan distance as a heuristic and Euclidean distance as heuristic, respectively.
Both functions utilize the heapq library to implement a priority queue data structure.
Elements of the priority queue are tuples where the key is the state and the value is the
sum of its cost value and heuristic value.
Both functions initialize four dictionaries: parent_map, cost_map, heuristic_map, and f_map.
The f_map[element] is the sum of the cost_map[element] and the heuristic_map[element].
       *
**get_children(state):** This function swaps the “0” element with all possible adjacent
elements to get the children of a certain node. It returns a list with 2, 3, or 4 children.
       *
### Game.py
This class is to connect the GUI with the Puzzle class. It’s mainly a utility class so that the
buttons can work, and the states can be displayed. Notable functions:

**isSolvable(array):** This function calculates number of inversions. It returns true if there’s
an even number of inversions, and thus the initial state is solvable and it returns false if
there’s an odd number of inversions and thus the initial state is unsolvable.

### main.py
Driver class loading the UI file and executing the application.
