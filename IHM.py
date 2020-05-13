from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.__layout = QGridLayout()
        self.__label = QLabel("laisser un commentaire")
        self.__button = QPushButton("success")
        self.__button1 = QPushButton("cancel")
        self.__text = QTextEdit("")
        self.__layout.addWidget(self.__label)
        self.__layout.addWidget(self.__text)
        self.__layout.addWidget(self.__button)
        self.__layout.addWidget(self.__button1)
        self.setLayout(self.__layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
