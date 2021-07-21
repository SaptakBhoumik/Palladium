from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import concurrent.futures
import threading
import os
from web import web


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        # defining shotcuts
        self.setWindowTitle("PALLADIUM")
        self.setFixedSize(400, 620)
        self.setStyleSheet('background-color: white;color:white')
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view .setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.view.load(QtCore.QUrl("http://127.0.0.1:5000/lungs"))
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)
        self.setWindowIcon(QtGui.QIcon(os.path.join('images', 'source.jpeg')))
        



if __name__ == "__main__":
    import sys
    th = threading.Thread(target=web.run)
    th.daemon = True
    th.start()
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())