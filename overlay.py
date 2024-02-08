from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, pyqtSignal
import sys

class Overlay(QWidget):


    def __init__(self, x, y, w, h):
        super().__init__()
        self.setGeometry(x, y, w, h)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: rgba(255, 0, 0, 150);")
        self.show()

    def draw_rectangle(self, x, y, w, h):
        self.label.setGeometry(x, y, w, h)

    