from PyQt5 import QtWidgets
import sys
from gui.app import App

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())