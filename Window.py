from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__layoutVertical = QVBoxLayout()
        self.__label = QLabel("label")
        self.__button = QPushButton("bouton")
        self.__text = QTextEdit("text")
        self.__layoutVertical.addWidget(self.__label)
        self.__layoutVertical.addWidget(self.__button)
        self.__layoutVertical.addWidget(self.__text)
        self.setLayout(self.__layoutVertical)

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()

