import sys

print(sys.executable)

import PyQt5
from PyQt5.QWidgets import *





if __name__=='__main__':
	hello=QApplication([])
	finestra=QMainWindow()
	label=QLabel('Hello, World!')
	finestra.setCentralWidget(label)
	finestra.show()
	hello.exec_()