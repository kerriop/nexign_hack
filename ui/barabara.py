import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWebEngineWidgets import QWebEngineView
from arcgis.gis import GIS

class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()

app = QtWidgets.QApplication(sys.argv)
b = Browser()
my_gis = GIS()
# b.load(QtCore.QUrl.fromLocalFile('test_map.html'))
b.load(QtCore.QUrl('https://www.arcgis.com'))
# b.load(QtCore.QUrl(m))
# b.load(QtCore.QUrl.fromLocalFile(QDir.current().filePath('test_map.html')))
b.show()
app.exec_()