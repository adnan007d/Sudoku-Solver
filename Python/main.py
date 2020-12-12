from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QLine, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.uic import loadUi
from sudoku import Sudoku
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi('Sudoku_Solver.ui',self)
        self.initUI()
    
    def initUI(self):
        self.solved = []
        self.Grid = [
            [self.l00, self.l01, self.l02, self.l03, self.l04, self.l05, self.l06, self.l07, self.l08],
            [self.l10, self.l11, self.l12, self.l13, self.l14, self.l15, self.l16, self.l17, self.l18],
            [self.l20, self.l21, self.l22, self.l23, self.l24, self.l25, self.l26, self.l27, self.l28],
            [self.l30, self.l31, self.l32, self.l33, self.l34, self.l35, self.l36, self.l37, self.l38],
            [self.l40, self.l41, self.l42, self.l43, self.l44, self.l45, self.l46, self.l47, self.l48],
            [self.l50, self.l51, self.l52, self.l53, self.l54, self.l55, self.l56, self.l57, self.l58],
            [self.l60, self.l61, self.l62, self.l63, self.l64, self.l65, self.l66, self.l67, self.l68],
            [self.l70, self.l71, self.l72, self.l73, self.l74, self.l75, self.l76, self.l77, self.l78],
            [self.l80, self.l81, self.l82, self.l83, self.l84, self.l85, self.l86, self.l87, self.l88],
        ]
        for i in range(9):
            for j in range(9):
                self.Grid[i][j].setAlignment(Qt.AlignHCenter)
                self.Grid[i][j].setValidator(QIntValidator(1,9,self))
                self.Grid[i][j].setMaxLength(1)
        self.solveButton.clicked.connect(self.solve)
        self.clearButton.clicked.connect(self.clear)
    

    def solve(self):
        for i in range(9):
            self.solved.append([])
            for j in range(9):
                temp = self.Grid[i][j].text()
                if temp.strip() == '':
                    self.solved[i].append(0)
                else:
                    self.solved[i].append(int(temp))

        sudoku = Sudoku(self.solved)
        if sudoku.solve():
            for i in range(9):
                for j in range(9):
                    self.Grid[i][j].setText(str(self.solved[i][j]))
            self.label.setStyleSheet("color:green;")
            self.label.setText("Solved!!!")
        else:
            self.label.setStyleSheet("color:red;")
            self.label.setText("No solution available!!!")

    def clear(self):
        del(self.solved[:])
        for i in range(9):
            for j in range(9):
                self.Grid[i][j].clear()
        self.label.setText("")

app = QApplication(sys.argv)
win = MainWindow()
win.setFixedWidth(452)
win.setFixedHeight(559)
win.show()
sys.exit(app.exec_())