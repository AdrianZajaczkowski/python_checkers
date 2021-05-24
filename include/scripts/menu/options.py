import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Options(QWidget):
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

        self.label = QLabel('Options',self)
        self.label.resize(120,120)
        self.label.move(int(self.width/2)-30, 50)
        self.label.setAlignment(Qt.AlignVCenter)

        self.layout = QPushButton("Change Layout",self)
        self.layout.move(int(self.width/2)-30, int(self.height/2)-50)
        self.layout.clicked.connect(self._layout)

        self.back = QPushButton("Back To Menu",self)
        self.back.move(int(self.width/2)-30, int(self.height/2)+20)
        self.back.clicked.connect(self._back)

        self.show()

    def _layout(self):
        pass
    def _back(self):
        pass
def main():
    app = QApplication(sys.argv)
    options = Options()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()