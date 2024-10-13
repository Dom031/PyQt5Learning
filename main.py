# Intro to PyQt5 for my Final Year Project
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Window")
        self.setGeometry(1000,300,500,500)
        icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon', 'logo-no-background.png')

        self.setWindowIcon(QIcon(icon_path))
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 
    #using app.exec_ to ensure the window stays open till interacted with
    #otherwise it closes in less than a second        
        
if __name__ == "__main__":
    main()