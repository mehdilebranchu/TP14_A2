from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setFixedSize(400,300)
        self.myicon = QIcon("drapeau.png")
        self.setWindowIcon(self.myicon)
        self.__layout = QVBoxLayout()
        self.__label = QLabel("laisser un commentaire")
        self.__label.setAlignment(Qt.AlignCenter)
        self.__bar = QProgressBar()
        self.__bar.setValue(50)
        self.__line = QLineEdit()
        self.__button = QPushButton('Click me')
        self.__button.setToolTip('veuillez patienter')
        self.__layout.addWidget(self.__label)
        self.__layout.addWidget(self.__bar)
        self.__layout.addWidget(self.__line)
        self.__layout.addWidget(self.__button)
        self.setLayout(self.__layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
