from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QPushButton, QRadioButton, QLineEdit
from Puzzle import Puzzle

class Game:

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

        self.lineEdit = self.ui.findChild(QLineEdit, 'lineEdit')

        self.buttonRun.clicked.connect(self.run)
        self.buttonNext.clicked.connect(self.next)
        self.buttonPrev.clicked.connect(self.prev)
        self.buttonSkipNext.clicked.connect(self.skip_next)
        self.buttonSkipPrev.clicked.connect(self.skip_prev)



    def get_path(self, state):
        path = []
        path.append(state)
        while state.parent is not None:
            state = state.parent
            path.append(state)
        return path

    def print_state(self, state):
        self.label0.setText(str(state.array[0]))
        self.label1.setText(str(state.array[1]))
        self.label2.setText(str(state.array[2]))
        self.label3.setText(str(state.array[3]))
        self.label4.setText(str(state.array[4]))
        self.label5.setText(str(state.array[5]))
        self.label6.setText(str(state.array[6]))
        self.label7.setText(str(state.array[7]))
        self.label8.setText(str(state.array[8]))

    def run(self):
        initial_values = []
        initial_string = self.lineEdit.text()
        initial_string = initial_string.split()
        for element in initial_string:
            initial_values.append(int(element))
        puzzle = Puzzle(initial_values)
        if self.radioBFS.isChecked():
            self.goal_state = puzzle.BFS()
        elif self.radioDFS.isChecked():
            self.goal_state = puzzle.DFS()
        elif self.radioASTARMAN.isChecked():
            self.goal_state = puzzle.A_star(1)
        elif self.radioASTAREUC.isChecked():
            self.goal_state = puzzle.A_star(2)
        self.display(self.goal_state)

    def display(self, state):
        self.states_path = self.get_path(state)
        self.state_index = len(self.states_path) - 1
        self.print_state(self.states_path[self.state_index])
        string = '1/' + str(len(self.states_path))
        self.pathNodes.setText(string)

    def prev(self):
        if len(self.states_path) > self.state_index + 1:
            self.state_index = self.state_index + 1
            self.print_state(self.states_path[self.state_index])
            string = str(len(self.states_path)-self.state_index) +'/' + str(len(self.states_path))
            self.pathNodes.setText(string)
        return

    def next(self):
        if self.state_index > 0:
            self.state_index = self.state_index - 1
            self.print_state(self.states_path[self.state_index])
            string = str(len(self.states_path)-self.state_index) + '/' + str(len(self.states_path))
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
