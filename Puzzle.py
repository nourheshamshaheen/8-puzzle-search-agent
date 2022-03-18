from collections import deque
import heapq
from State import State

class Puzzle:
    def __init__(self, initial_values):
        self.goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.initial_state = State(None, initial_values, 0)
        self.initial_state_man = State(None, initial_values, 1)
        self.initial_state_euc = State(None, initial_values, 2)

    #compare state w/ goal state to test for success
    def goal_test(self, state):
        if state.array == self.goal_state:
            return True
        return False

    def BFS(self):
        frontier = deque()  # frontier is a FIFO queue: append: enqueue, popleft: dequeue
        frontier.append(self.initial_state)
        explored = []

        while frontier: # while frontier queue is not empty (yields true)
            print(len(frontier))
            state = frontier.popleft()
            explored.append(state.array)

            if self.goal_test(state):
                return state

            children = state.get_children()
            for child in children:
                if not self.exists(child, frontier) and child.array not in explored:
                    frontier.append(child)
        return None

    def DFS(self):
        frontier = deque()  # frontier is a LIFO stack: append: PUSH, pop: POP
        frontier.append(self.initial_state)
        explored = []

        while frontier: # while frontier stack is not empty (yields true)
            state = frontier.pop()
            explored.append(state.array)

            if self.goal_test(state):
                return state

            children = state.get_children()
            for child in children:
                if child not in frontier and child.array not in explored:
                    frontier.append(child)
        return None

    def A_star(self, type): # type is 1 for manhattan and 2 for euclidean

        if type == 1:
            frontier = [self.initial_state_man] # frontier is a priority queue/minheap
        if type == 2:
            frontier = [self.initial_state_euc]

        heapq.heapify(frontier)
        explored = []

        while frontier: # while frontier priority queue is not empty (yields true)
            state = heapq.heappop(frontier)
            explored.append(state.array)

            if self.goal_test(state):
                return state

            children = state.get_children()
            for child in children:
                if not self.exists(child, frontier) and child.array not in explored:
                    heapq.heappush(frontier, child)
                elif self.exists(child, frontier):
                    index = self.get_index(child, frontier)
                    if frontier[index] > child:
                        frontier[index] = child
                        heapq.heapify(frontier)
        return None

    def exists(self, element, mylist):
        for i in mylist:
            if element.array == i.array:
                return True
        return False

    def get_index(self, element, mylist):
        for i in mylist:
            if element.array == i.array:
                return mylist.index(i)
        return None