import arcgis
from arcgis.gis import GIS
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtNetwork import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon

import arcgis
from arcgis.gis import GIS
import arcgis.geocoding as geocoding
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import osmapi
import csv
import pandas as pd


class MyBrowser(QWebEnginePage):
    """ Settings for the browser."""

    def userAgentForUrl(self, url):
        """ Returns a User Agent that will be seen by the website. """
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"


class Browser(QWebEngineView):
    def __init__(self):
        # QWebView
        self.view = QWebEngineView.__init__(self)
        # self.view.setPage(MyBrowser())
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        # super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.adjustTitle)

    def load(self, url):
        self.setUrl(QUrl(url))

    def adjustTitle(self):
        self.setWindowTitle(self.title())

        # def disableJS(self):
        #     settings = QWebSettings.globalSettings()
        #     settings.setAttribute(QWebSettings.JavascriptEnabled, False)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # m = PlotCanvas(self, width=5, height=4)
        m = Map(self)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500, 0)
        button.resize(140, 100)

        self.show()


class Map():
    def __init__(self):
        my_gis = GIS()
        global hello_map
        hello_map = my_gis.map('Санкт-Петербург', zoomlevel=15)
        hello_map.basemap = 'osm'

        # ============
        def find_addr(hello_map, g):
            #     try:
            hello_map.draw(g)
            global address
            geocoded = geocoding.reverse_geocode(g)
            address = geocoded['address']['Match_addr']
            # adres_read = Adres_read(address)
            # print(adres_read.get_points())

            try:
                print('creating')
                # a = Osm_reader(adres_read.get_points())
                # a.create_file()
                print('file created')
            except:
                print("beda")

        hello_map.on_click(address)
        # hello_map.on_click(find_addr)
        # ============

        # hello_map.export_to_html('test_map.html')

# ===========
# class Adres_read():
#     def __init__(self, adress):
#         self.__geolocator = Nominatim(user_agent="specify_your_app_name_here")
#         self.__location = self.__geolocator.geocode(adress)
#         # self.__location_place = (self.__location.latitude, self.__location.longitude)
#
#         self.__bounding = self.__location.raw['boundingbox']
#
#     def get_points(self):
#         return self.__bounding
#
#
# class Osm_reader():
#     #     def __init__(self, min_lon, min_lat, max_lon, max_lat):
#     def __init__(self, lil):
#         #         print(lil)
#         self.__api = osmapi.OsmApi()
#         #         self.__tmp = self.__api.Map(min_lon, min_lat, max_lon, max_lat)
#         self.__tmp = self.__api.Map(float(lil[2]), float(lil[0]), float(lil[3]), float(lil[1]))
#         self.__ret = []
#
#         for e in self.__tmp:
#             try:
#                 try:
#                     try:
#                         type_ = e['type']
#                         timestamp = e['data']['timestamp']
#                         id = e['data']['id']
#                         lat = e['data']['lat']
#                         lon = e['data']['lon']
#                         uid = e['data']['uid']
#                         user = str(e['data']['user'])
#                         tag = e['data']['tag']
#                         delta_days = (osmapi.datetime.today() - timestamp).days
#
#                         if type_ == 'node':
#                             self.__ret.append([id, lat, lon, uid, timestamp, user])
#
#                     except KeyError:
#                         pass
#                 except IndexError:
#                     pass
#             except UnicodeEncodeError as err:
#                 print(err, str(e) + '\n')
#
#     def create_file(self):
#         with open('dumps.csv', "w", newline='', encoding='utf-8') as csv_file:
#             writer = csv.writer(csv_file, delimiter=',')
#             for line in self.__ret:
#                 #                 print(line)
#                 writer.writerow(line)
#
#             csv_file.close()
#
#     def get_values(self):
#         return self.__ret
#
# def find_addr(hello_map, g):
# #     try:
#     hello_map.draw(g)
#     geocoded = geocoding.reverse_geocode(g)
#     address = geocoded['address']['Match_addr']
#     adres_read = Adres_read(address)
#     print(adres_read.get_points())
#
#     try:
#         print('creating')
#         a = Osm_reader(adres_read.get_points())
#         a.create_file()
#         print('file created')
#     except:
#         print("beda")
# hello_map.on_click(find_addr)
# ============

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Browser()
    view.showMaximized()
    view.load('https://www.arcgis.com')
    # view.load('test_map.html')
    app.exec_()

    # app = QApplication(sys.argv)
    # ex = App()
    # sys.exit(app.exec_())
