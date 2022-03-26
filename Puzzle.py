import math
from collections import deque
import heapq

class Puzzle:
    def __init__(self, initial_state):
        self.goal_state = "012345678"
        self.initial_state = initial_state
        self.solvable = True

    #compare state w/ goal state to test for success
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        return False

    # How to get children? Try every swap between the '0' element and the element next to it
    def get_children(self, state):
        children = []
        index = state.find('0')  # find zero index to determine swaps with other elements
        if index not in [0, 3, 6]:
            child = self.swap_left(state, index)
            children.append(child)
        if index not in [2, 5, 8]:
            child = self.swap_right(state, index)
            children.append(child)
        if index not in [0, 1, 2]:
            child = self.swap_up(state, index)
            children.append(child)
        if index not in [6, 7, 8]:
            child = self.swap_down(state, index)
            children.append(child)
        return children

    def BFS(self):
        expanded_nodes = 0
        frontier = deque()  # frontier is a FIFO queue: append: enqueue, popleft: dequeue
        frontier.append(self.initial_state)
        explored = set()
        parent_map = {self.initial_state: None}
        cost_map = {self.initial_state: 0}

        while frontier:  # while frontier queue is not empty (yields true)
            print(len(frontier))
            state = frontier.popleft()
            expanded_nodes += 1
            explored.add(state)

            if self.goal_test(state):
                self.solvable = True
                print("BFS expanded nodes: " + str(expanded_nodes))
                return state, parent_map, cost_map

            children = self.get_children(state)
            for child in children:
                if child not in frontier and child not in explored:
                    frontier.append(child)
                    parent_map[child] = state
                    cost_map[child] = cost_map[state] + 1
        self.solvable = False
        print("BFS expanded nodes: " + str(expanded_nodes))
        return None, parent_map, cost_map

    def DFS(self):
        expanded_nodes = 0
        frontier = deque()  # frontier is a LIFO stack: append: push, pop: pop
        frontier.append(self.initial_state)
        explored = set()
        parent_map = {self.initial_state: None}
        cost_map = {self.initial_state: 0}

        while frontier:  # while frontier queue is not empty (yields true)
            print(len(frontier))
            state = frontier.pop()
            expanded_nodes += 1
            explored.add(state)

            if self.goal_test(state):
                self.solvable = True
                print("DFS expanded nodes: " + str(expanded_nodes))
                return state, parent_map, cost_map

            children = self.get_children(state)
            for child in children:
                if child not in frontier and child not in explored:
                    frontier.append(child)
                    parent_map[child] = state
                    cost_map[child] = cost_map[state] + 1

        self.solvable = False
        print("DFS expanded nodes: " + str(expanded_nodes))
        return None, parent_map, cost_map

    def A_star_man(self):
        expanded_nodes = 0
        explored = set()
        parent_map = {self.initial_state: None}
        cost_map = {self.initial_state: 0}
        heuristic_map = {self.initial_state: self.get_man_h(self.initial_state)}
        f_map = {self.initial_state: self.get_man_h(self.initial_state)}
        frontier = []  # frontier is a priority queue/minheap
        heapq.heappush(frontier, (f_map[self.initial_state], self.initial_state))

        while frontier:  # while frontier priority queue is not empty (yields true)
            current_cost, state = heapq.heappop(frontier)
            print(str(len(frontier)))
            expanded_nodes += 1
            explored.add(state)

            if self.goal_test(state):
                self.solvable = True
                print("A* (manhattan) expanded nodes: " + str(expanded_nodes))
                return state, parent_map, cost_map

            children = self.get_children(state)
            for child in children:
                if child not in frontier and child not in explored:
                    parent_map[child] = state
                    cost_map[child] = cost_map[state] + 1
                    heuristic_map[child] = self.get_man_h(child)
                    f_map[child] = cost_map[child] + heuristic_map[child]
                    heapq.heappush(frontier, (f_map[child], child))
                elif child in frontier:
                    if cost_map[state] + 1 < cost_map[child]:
                        frontier.remove((f_map[child], child))
                        parent_map[child] = state
                        cost_map[child] = cost_map[state] + 1
                        heuristic_map[child] = self.get_man_h(child)
                        f_map[child] = cost_map[child] + heuristic_map[child]
                        heapq.heappush(frontier, (f_map[child], child))
                        heapq.heapify(frontier)
        self.solvable = False
        print("A* (manhattan) expanded nodes: " + str(expanded_nodes))
        return None, parent_map, cost_map

    def A_star_euc(self):
        explored = set()
        expanded_nodes = 0
        parent_map = {self.initial_state: None}
        cost_map = {self.initial_state: 0}
        heuristic_map = {self.initial_state: self.get_euc_h(self.initial_state)}
        f_map = {self.initial_state: self.get_euc_h(self.initial_state)}

        frontier = []  # frontier is a priority queue/minheap
        heapq.heappush(frontier, (f_map[self.initial_state], self.initial_state))

        while frontier:  # while frontier priority queue is not empty (yields true)
            current_cost, state = heapq.heappop(frontier)
            print(str(len(frontier)))
            explored.add(state)
            expanded_nodes += 1

            if self.goal_test(state):
                self.solvable = True
                print("A* (euclidean) expanded nodes: " + str(expanded_nodes))
                return state, parent_map, cost_map

            children = self.get_children(state)
            for child in children:
                if child not in frontier and child not in explored:
                    parent_map[child] = state
                    cost_map[child] = cost_map[state] + 1
                    heuristic_map[child] = self.get_euc_h(child)
                    f_map[child] = cost_map[child] + heuristic_map[child]
                    heapq.heappush(frontier, (f_map[child], child))
                elif child in frontier:
                    if cost_map[state] + 1 < cost_map[child]:
                        parent_map[child] = state
                        cost_map[child] = cost_map[state] + 1
                        heuristic_map[child] = self.get_man_h(child)
                        f_map[child] = cost_map[child] + heuristic_map[child]
                        heapq.heappush(frontier, (f_map[child], child))
        self.solvable = False
        print("A* (euclidean) expanded nodes: " + str(expanded_nodes))
        return None, parent_map, cost_map

    # functions to swap 0 for elements around it:

    def swap_right(self, state, index):
        new_state = ""
        for character in range(0, len(state)):
            if len(new_state) == (index+1):
                new_state += state[index]
            elif len(new_state) == index:
                new_state += state[index+1]
            else:
                new_state += state[character]
        return new_state

    def swap_left(self, state, index):
        new_state = ""
        for character in range(0, len(state)):
            if len(new_state) == (index - 1):
                new_state += state[index]
            elif len(new_state) == index:
                new_state += state[index - 1]
            else:
                new_state += state[character]
        return new_state

    def swap_up(self, state, index):
        new_state = ""
        for character in range(0, len(state)):
            if len(new_state) == (index - 3):
                new_state += state[index]
            elif len(new_state) == index:
                new_state += state[index - 3]
            else:
                new_state += state[character]
        return new_state

    def swap_down(self, state, index):
        new_state = ""
        for character in range(0, len(state)):
            if len(new_state) == (index + 3):
                new_state += state[index]
            elif len(new_state) == index:
                new_state += state[index + 3]
            else:
                new_state += state[character]
        return new_state

    # functions to calculate heruistic for certain state:

    def get_man_h(self, state):
        # goal_state = "012345678"
        initial_config = state
        man_distance = 0
        for i, item in enumerate(initial_config):
            if not int(i) == 0:
                prev_row, prev_col = int(i / 3), i % 3
                goal_row, goal_col = int(int(item) / 3), int(item) % 3
                man_distance += abs(prev_row - goal_row) + abs(prev_col - goal_col)
        return man_distance

    def get_euc_h(self, state):
        #goal_state = "012345678"
        initial_config = state
        euc_distance = 0
        for i, item in enumerate(initial_config):
            if not int(i) == 0:
                current_row, current_col = int(i / 3), i % 3
                goal_row, goal_col = int(int(item) / 3), int(item) % 3
                euc_distance += math.sqrt((current_row - goal_row)*(current_row - goal_row) + (current_col - goal_col)*(current_col - goal_col))
        return euc_distance