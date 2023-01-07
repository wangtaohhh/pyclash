from PyQt5 import QtWidgets
import sys
import subprocess

class ClashMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("pyclash")
        self.resize(900, 750)

        self.layout = QtWidgets.QFormLayout()
        self.proxies_list = QtWidgets.QTableWidget(self)
        










if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ClashMainWindow()
    window.show()

    sys.exit(app.exec_())






















