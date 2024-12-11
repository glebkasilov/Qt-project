from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class Error_Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/style/Helpfull_windows/error.ui', self)
