from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QPushButton, QRadioButton, QLineEdit
from Puzzle import Puzzle
from datetime import datetime as time


class Game:  # GUI Driver class

    def __init__(self, ui):
        self.ui = ui
        self.radioBFS = self.ui.findChild(QRadioButton, 'radioBFS')
        self.radioDFS = self.ui.findChild(QRadioButton, 'radioDFS')
        self.radioASTARMAN = self.ui.findChild(QRadioButton, 'radioASTARMAN')
        self.radioASTAREUC = self.ui.findChild(QRadioButton, 'radioASTAREUC')

        self.state_index = 0
        self.states_path = []

        self.buttonNext = self.ui.findChild(QPushButton, 'buttonNext')
        self.buttonPrev = self.ui.findChild(QPushButton, 'buttonPrev')
        self.buttonSkipNext = self.ui.findChild(QPushButton, 'buttonSkipNext')
        self.buttonSkipPrev = self.ui.findChild(QPushButton, 'buttonSkipPrev')
        self.buttonRun = self.ui.findChild(QPushButton, 'buttonRun')

        self.pathNodes = self.ui.findChild(QLabel, 'pathNodes')

        self.label0 = self.ui.findChild(QLabel, 'label0')
        self.label1 = self.ui.findChild(QLabel, 'label1')
        self.label2 = self.ui.findChild(QLabel, 'label2')
        self.label3 = self.ui.findChild(QLabel, 'label3')
        self.label4 = self.ui.findChild(QLabel, 'label4')
        self.label5 = self.ui.findChild(QLabel, 'label5')
        self.label6 = self.ui.findChild(QLabel, 'label6')
        self.label7 = self.ui.findChild(QLabel, 'label7')
        self.label8 = self.ui.findChild(QLabel, 'label8')

        self.label0.setText(" ")
        self.lineEdit = self.ui.findChild(QLineEdit, 'lineEdit')
        self.lineEdit.setText("125340678")

        self.buttonRun.clicked.connect(self.run)
        self.buttonNext.clicked.connect(self.next)
        self.buttonPrev.clicked.connect(self.prev)
        self.buttonSkipNext.clicked.connect(self.skip_next)
        self.buttonSkipPrev.clicked.connect(self.skip_prev)

    def get_path(self, final_state, parent_map):  # getting path from parent map and goal state
        path = [final_state]
        state = parent_map[final_state]
        while state is not None:
            path.append(state)
            state = parent_map[state]
        return path

    def print_state(self, final_state):  # utility function to display states on GUI board
        state = ""
        for character in final_state:
            if character != '0':
                state += character
            else:
                state += ' '

        self.label0.setText(str(state[0]))
        self.label1.setText(str(state[1]))
        self.label2.setText(str(state[2]))
        self.label3.setText(str(state[3]))
        self.label4.setText(str(state[4]))
        self.label5.setText(str(state[5]))
        self.label6.setText(str(state[6]))
        self.label7.setText(str(state[7]))
        self.label8.setText(str(state[8]))

    def get_inversions(self, array):  # function to get number of inversions in certain state
        inv_count = 0
        empty_value = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if array[j] != empty_value and array[i] != empty_value and array[i] > array[j]:
                    inv_count += 1
        return inv_count

    def isSolvable(self, puzzle):
        inv_count = self.get_inversions([j for sub in puzzle for j in sub])
        return (inv_count % 2 == 0)

    def run(self):  # main function running the chosen algorithm
        initial_string = self.lineEdit.text()
        arr = [[int(initial_string[0]), int(initial_string[1]), int(initial_string[2])],
               [int(initial_string[3]), int(initial_string[4]), int(initial_string[5])],
               [int(initial_string[6]), int(initial_string[7]), int(initial_string[8])]]
        print("Solvability check using function: " + str(self.isSolvable(arr)))
        if not self.isSolvable(arr):
            return
        puzzle = Puzzle(initial_string)
        if self.radioBFS.isChecked():
            start = time.now()
            goal_state, parent_map, cost_map = puzzle.BFS()
            end = time.now()
            print("BFS running time (in millis) = " + str((end - start).microseconds / 1000))
        elif self.radioDFS.isChecked():
            start = time.now()
            goal_state, parent_map, cost_map = puzzle.DFS()
            end = time.now()
            print("DFS running time (in millis) = " + str((end - start).microseconds / 1000))
        elif self.radioASTARMAN.isChecked():
            start = time.now()
            goal_state, parent_map, cost_map = puzzle.A_star_man()
            end = time.now()
            print("A* man running time (in millis) = " + str((end - start).microseconds / 1000))
        elif self.radioASTAREUC.isChecked():
            start = time.now()
            goal_state, parent_map, cost_map = puzzle.A_star_euc()
            end = time.now()
            print("A* euc running time (in millis) = " + str((end - start).microseconds / 1000))
        if puzzle.solvable is True:
            self.display(goal_state, parent_map)
            print("SEARCH DEPTH IS: ", max(cost_map.values()))
        else:
            print("UNSOLVABLE")

    def display(self, state, parent_map):
        self.states_path = self.get_path(state, parent_map)
        self.state_index = len(self.states_path) - 1
        self.print_state(self.states_path[self.state_index])
        string = '1/' + str(len(self.states_path))
        self.pathNodes.setText(string)

    # functions to define what arrows do:

    def prev(self):
        if len(self.states_path) > self.state_index + 1:
            self.state_index = self.state_index + 1
            self.print_state(self.states_path[self.state_index])
            string = str(len(self.states_path) - self.state_index) + '/' + str(len(self.states_path))
            self.pathNodes.setText(string)
        return

    def next(self):
        if self.state_index > 0:
            self.state_index = self.state_index - 1
            self.print_state(self.states_path[self.state_index])
            string = str(len(self.states_path) - self.state_index) + '/' + str(len(self.states_path))
            self.pathNodes.setText(string)
        return

    def skip_next(self):
        self.state_index = 0
        self.print_state(self.states_path[0])
        string = str(len(self.states_path)) + '/' + str(len(self.states_path))
        self.pathNodes.setText(string)
        return

    def skip_prev(self):
        self.state_index = len(self.states_path) - 1
        self.print_state(self.states_path[self.state_index])
        string = '1/' + str(len(self.states_path))
        self.pathNodes.setText(string)
        return
