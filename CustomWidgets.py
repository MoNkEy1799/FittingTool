from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QGridLayout, QPushButton, QCheckBox
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fitting Tool")
        
        pg.setConfigOption("background", "#41444c")
        pg.setConfigOption("foreground", "#c4c4c4")
        pg.setConfigOptions(antialias=True)
        
        self.plot = pg.plot([1, 2, 3], [3, 4, 5])
        self.plot.getPlotItem()
        
        self.sidebar = SideBar(self)
        
        self.makeLayout()
        
        self.setStyleSheet(self.getStyleSheet("styleSheet.txt"))
        
    def makeLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.sidebar)
        layout.addWidget(self.plot)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
    def getStyleSheet(self, path):
        with open(path) as file:
            return file.read()
        
        
class SideBar(QWidget):
    def __init__(self, main):
        super().__init__()
        
        self.mainWindow = main
        
        self.button = QPushButton("test")
        self.check = QCheckBox()
        
        self.makeLayout()
        
    def makeLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.check)
        
        self.setLayout(layout)

        