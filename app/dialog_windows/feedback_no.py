from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class Feedback_Window_No(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/style/Helpfull_windows/feedback_tg.ui', self)
    