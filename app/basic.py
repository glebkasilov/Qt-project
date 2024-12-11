import requests

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QTimer

from app.server_part import ServerPartRepository
from app.database.repository import PictureRepository


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/style/main_window.ui', self)

        self.actionOpen_window_login.triggered.connect(self.login_window)

        self.generate_button.clicked.connect(self.gerate_picture)
        
        self.feedback_button.clicked.connect(self.feedback_window)

        self.id_request = 0

        self.flag_is_ready_picture = True

    def gerate_picture(self):
        if not self.checkBox.isChecked():
            text_to_generate = self.plainTextEdit.toPlainText()
            if text_to_generate == "" or text_to_generate == "Describe image you want here, for example: An astronaut riding a green horse":
                self.picture.setText("Invalid request")
                self.picture.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
                self.picture.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
            else:
                if self.flag_is_ready_picture:
                    global id_request
                    self.flag_is_ready_picture = False
                    id_request = ServerPartRepository.send_request(
                        text_to_generate)
                    self.generate_button.setText("Wait")
                    self.picture.setText("Generating...")

                    QTimer.singleShot(30_000, self.generate_picture_function)

        else:
            self.picture.setText("There is no connection to server")
            self.picture.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.picture.setAlignment(Qt.AlignmentFlag.AlignCenter)
            print("Invalid request")
            self.error_window()

    def generate_picture_function(self) -> None:
        self.picture.setText("Ready")
        self.generate_button.setText("Generate")

        self.flag_is_ready_picture = True

        with open('app/settings.txt', 'r') as file:
            login = file.read().strip()

        if id_request != 0:
            id, image_url = ServerPartRepository.get_request(id_request)
            if image_url == None:
                self.picture.setText("Bad request, try again")
                self.picture.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
                self.picture.setAlignment(Qt.AlignmentFlag.AlignCenter)

                print("Invalid request")
                self.error_window()
                
                PictureRepository.add_picture(
                    {"id_picture": id, "login": login, "directory": '-'})
                return
                

            else:
                img_data = requests.get(image_url).content
                with open(f'./app/photos_generated/image_{id}.jpg', 'wb') as handler:
                    handler.write(img_data)

                self.picture.setPixmap(QtGui.QPixmap(
                    f'./app/photos_generated/image_{id}.jpg'))
                self.picture.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.id_request = 0

                self.url_picture.setText('Image_url: ' + image_url)
                self.url_picture.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
                self.url_picture.setAlignment(Qt.AlignmentFlag.AlignCenter)

                PictureRepository.add_picture(
                    {"id_picture": id, "login": login, "directory": f'./app/photos_generated/image_{id}.jpg'})

        else:
            self.picture.setText("Bad request, try again")
            self.picture.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.picture.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def login_window(self):
        from __main__ import Window
        self.login_wn = Window()
        self.login_wn.show()
        Main_Window.hide(self)

    def error_window(self):
        from app.dialog_windows.error import Error_Window
        self.error_wn = Error_Window()
        self.error_wn.show()
    
    def feedback_window(self):
        from app.dialog_windows.feedback import Feedback_Window
        self.feedback_wn = Feedback_Window()
        self.feedback_wn.show()