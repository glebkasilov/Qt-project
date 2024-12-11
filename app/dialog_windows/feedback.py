from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class Feedback_Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/style/Helpfull_windows/feedback_dialog.ui', self)
    
        self.yes_button.clicked.connect(self.yes)
        self.no_button.clicked.connect(self.no)
    
    def yes(self):
        from app.dialog_windows.feedback_yes import Feedback_Window_Yes
        self.feedback_wn = Feedback_Window_Yes()
        self.feedback_wn.show()
        self.close()
    
    def no(self):
        from app.dialog_windows.feedback_no import Feedback_Window_No
        self.feedback_wn = Feedback_Window_No()
        self.feedback_wn.show()
        self.close()