import math

class State:
    def __init__(self, parent, array, heuristic):
        #if heuristic = 1: manhattan distance, if heuristic = 2: euclidean, else: uninformed search
        self.parent = parent
        self.array = array
        self.heuristic = heuristic
        if parent is None:
            self.cost = 0
            self.h_man = self.get_man_h()
            self.h_euc = self.get_euc_h()
        else:
            self.cost = parent.cost + 1
            self.h_man = parent.h_man + self.get_man_h()
            self.h_euc = parent.h_euc + self.get_euc_h()

    def __lt__(self, nxt):
        if self.heuristic == 1:
            return (self.h_man + self.cost) < (nxt.h_man + nxt.cost)
        elif self.heuristic == 2:
            return (self.h_euc + self.cost) < (nxt.h_euc + nxt.cost)

    # How to get children? Try every swap between the '0' element and the element next to it
    def get_children(self):
        children = []
        index = self.array.index(0)  # find zero index to determine swaps with other elements
        if index not in [2, 5, 8]:
            child = State(self, self.swap_right(self.array, index), self.heuristic)
            children.append(child)
        if index not in [0, 3, 6]:
            child = State(self, self.swap_left(self.array, index), self.heuristic)
            children.append(child)
        if index not in [0, 1, 2]:
            child = State(self, self.swap_up(self.array, index), self.heuristic)
            children.append(child)
        if index not in [6, 7, 8]:
            child = State(self, self.swap_down(self.array, index), self.heuristic)
            children.append(child)
        return children

    def swap_right(self, state, index):
        new_state = state.copy()
        new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
        return new_state

    def swap_left(self, state, index):
        new_state = state.copy()
        new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
        return new_state

    def swap_up(self, state, index):
        new_state = state.copy()
        new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
        return new_state

    def swap_down(self, state, index):
        new_state = state.copy()
        new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
        return new_state

    def get_man_h(self):
        goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        initial_config = self.array
        man_distance = 0
        for i, item in enumerate(initial_config):
            prev_row, prev_col = int(i / 3), i % 3
            goal_row, goal_col = int(item / 3), item % 3
            man_distance += abs(prev_row - goal_row) + abs(prev_col - goal_col)
        return man_distance

    def get_euc_h(self):
        goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        initial_config = self.array
        euc_distance = 0
        for i, item in enumerate(initial_config):
            prev_row, prev_col = int(i / 3), i % 3
            goal_row, goal_col = int(item / 3), item % 3
            euc_distance += math.sqrt((prev_row - goal_row)*(prev_row - goal_row) + (prev_col - goal_col)*(prev_col - goal_col))
        return euc_distance
