from PyQt4 import QtGui
import osxfullscreen
import sys

app = QtGui.QApplication(sys.argv)
win = QtGui.QWidget()
win.resize(400, 400)
win.setWindowTitle("Fullscreen Test")

win.show()

osxfullscreen.add_fullscreen_button(win)

sys.exit(app.exec_())
