import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    
    def initUi(self):

        self.top = 600
        self.left = 400
        self.width = 500
        self.height = 500
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Checkers")
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.label = QLabel('Main menu',self)
        self.label.resize(120,120)
        self.label.move(int(self.width/2)-30, 50)
        self.label.setAlignment(Qt.AlignVCenter)

        self.start = QPushButton("Start",self)
        self.start.move(int(self.width/2)-30, int(self.height/2)-50)
        self.start.clicked.connect(self._start)

        self.option = QPushButton("Option",self)
        self.option.move(int(self.width/2)-30, int(self.height/2)+20)
        self.option.clicked.connect(self._option)

        self.show()

    def _start(self):
        pass
    def _option(self):
        pass
def main():
    app = QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()