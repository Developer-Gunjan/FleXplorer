import typing
from cryptography.fernet import Fernet
import sys
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget
import zlib
from PyQt5.QtGui import QIcon
import subprocess
import pyautogui, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from send2trash import send2trash
from PyQt5.QtWidgets import QApplication, QAbstractItemView
import ctypes
import shutil
import psutil
import win32com

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-130, -28, 611, 61))
        self.label.setStyleSheet("background-color: rgb(0, 162, 232);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-4, 30, 451, 301))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.firstProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.firstProgressBar.setGeometry(QtCore.QRect(10, 90, 401, 23))
        self.firstProgressBar.setProperty("value", 0)
        self.firstProgressBar.setObjectName("firstProgressBar")
        self.processBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.processBrowser.setGeometry(QtCore.QRect(45, 30, 311, 31))
        self.processBrowser.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border:0px;")
        self.processBrowser.setObjectName("processBrowser")
        self.fileNameBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.fileNameBrowser.setGeometry(QtCore.QRect(55, 60, 291, 31))
        self.fileNameBrowser.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"border:0px;")
        self.fileNameBrowser.setObjectName("fileNameBrowser")
        self.firstTextLabel = QtWidgets.QTextBrowser(self.centralwidget)
        self.firstTextLabel.setGeometry(QtCore.QRect(20, 111, 291, 31))
        self.firstTextLabel.setStyleSheet("border:0px;")
        self.firstTextLabel.setObjectName("firstTextLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 142, 401, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 163, 256, 31))
        self.textBrowser.setStyleSheet("border:0px;")
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 212, 401, 21))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 231, 261, 31))
        self.textBrowser_2.setStyleSheet("border:0px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(324, 272, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.label.raise_()
        self.label_2.raise_()
        self.processBrowser.raise_()
        self.fileNameBrowser.raise_()
        self.firstTextLabel.raise_()
        self.firstProgressBar.raise_()
        self.textBrowser.raise_()
        self.progressBar.raise_()
        self.textBrowser_2.raise_()
        self.progressBar_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.processBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Decrypting...</p></body></html>"))
        self.fileNameBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">File - tt.txt</p></body></html>"))
        self.firstTextLabel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Encrypting...</p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Compressing...</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Decrypting...</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -31, 1366, 731))
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.item_widget_primary = QtWidgets.QListWidget(self.centralwidget)
        self.item_widget_primary.setGeometry(QtCore.QRect(0, 221, 1211, 411))
        self.item_widget_primary.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.item_widget_primary.setDragEnabled(True)
        self.item_widget_primary.setDragDropOverwriteMode(True)
        self.item_widget_primary.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.item_widget_primary.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.item_widget_primary.setUniformItemSizes(False)
        self.item_widget_primary.setObjectName("item_widget_primary")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("FOLDER - EMPTY.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon)
        self.item_widget_primary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("FOLDER - FULL.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon1)
        self.item_widget_primary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("file-icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon2)
        self.item_widget_primary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("file-icon - Decrypted.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon3)
        self.item_widget_primary.addItem(item)
        self.dir_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.dir_browser.setGeometry(QtCore.QRect(10, 180, 1201, 31))
        self.dir_browser.setReadOnly(True)
        self.dir_browser.setObjectName("dir_browser")
        self.searchBar = QtWidgets.QTextEdit(self.centralwidget)
        self.searchBar.setGeometry(QtCore.QRect(10, 640, 1051, 31))
        self.searchBar.setStyleSheet("QTextEdit,\n"
"QTextEdit::plaintext {\n"
"    font-size: 13pt;\n"
"}")
        self.searchBar.setAcceptRichText(True)
        self.searchBar.setObjectName("searchBar")
        self.item_widget_secondary = QtWidgets.QListWidget(self.centralwidget)
        self.item_widget_secondary.setGeometry(QtCore.QRect(1220, 210, 151, 461))
        self.item_widget_secondary.setDragEnabled(True)
        self.item_widget_secondary.setDragDropOverwriteMode(True)
        self.item_widget_secondary.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.item_widget_secondary.setObjectName("item_widget_secondary")
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("This PC.bmp"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon4)
        self.item_widget_secondary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Drive-icon.bmp"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon5)
        self.item_widget_secondary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon5)
        self.item_widget_secondary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon5)
        self.item_widget_secondary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon5)
        self.item_widget_secondary.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon5)
        self.item_widget_secondary.addItem(item)
        self.propertybrowser1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.propertybrowser1.setGeometry(QtCore.QRect(0, 20, 601, 151))
        self.propertybrowser1.setStyleSheet("background-color: transparent;")
        self.propertybrowser1.setObjectName("propertybrowser1")
        self.propertybrowser2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.propertybrowser2.setGeometry(QtCore.QRect(600, 21, 671, 151))
        self.propertybrowser2.setStyleSheet("background-color: transparent;")
        self.propertybrowser2.setObjectName("propertybrowser2")
        self.Delete_temporarily_button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_temporarily_button.setGeometry(QtCore.QRect(260, 680, 211, 20))
        self.Delete_temporarily_button.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Delete_temporarily_button.setObjectName("Delete_temporarily_button")
        self.Delete_permanently_button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_permanently_button.setGeometry(QtCore.QRect(750, 680, 211, 20))
        self.Delete_permanently_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Delete_permanently_button.setObjectName("Delete_permanently_button")
        self.Open_button = QtWidgets.QPushButton(self.centralwidget)
        self.Open_button.setGeometry(QtCore.QRect(500, 680, 221, 21))
        self.Open_button.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"")
        self.Open_button.setObjectName("Open_button")
        self.Decrypt_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Decrypt_Button.setGeometry(QtCore.QRect(990, 680, 211, 20))
        self.Decrypt_Button.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Decrypt_Button.setObjectName("Decrypt_Button")
        self.Encrypt_button = QtWidgets.QPushButton(self.centralwidget)
        self.Encrypt_button.setGeometry(QtCore.QRect(20, 680, 210, 21))
        self.Encrypt_button.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.Encrypt_button.setObjectName("Encrypt_button")
        self.Encrypt_All_button = QtWidgets.QPushButton(self.centralwidget)
        self.Encrypt_All_button.setGeometry(QtCore.QRect(1230, 680, 130, 21))
        self.Encrypt_All_button.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.Encrypt_All_button.setObjectName("Encrypt_All_button")
        self.navigate_back_button = QtWidgets.QPushButton(self.centralwidget)
        self.navigate_back_button.setGeometry(QtCore.QRect(1220, 170, 71, 41))
        self.navigate_back_button.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.navigate_back_button.setObjectName("navigate_back_button")
        self.navigate_next_button = QtWidgets.QPushButton(self.centralwidget)
        self.navigate_next_button.setGeometry(QtCore.QRect(1294, 170, 81, 41))
        self.navigate_next_button.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"background-color: transparent;")
        self.navigate_next_button.setObjectName("navigate_next_button")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(1280, 32, 31, 31))
        self.settings_button.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.settings_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("settings-icon1.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.settings_button.setIcon(icon6)
        self.settings_button.setIconSize(QtCore.QSize(29, 29))
        self.settings_button.setObjectName("settings_button")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(1070, 640, 121, 31))
        self.searchButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.searchButton.setObjectName("searchButton")
        self.appTitle = QtWidgets.QTextBrowser(self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(-5, 0, 1371, 31))
        self.appTitle.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:0px;")
        self.appTitle.setObjectName("appTitle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 700, 1381, 21))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.background.raise_()
        self.item_widget_primary.raise_()
        self.dir_browser.raise_()
        self.searchBar.raise_()
        self.item_widget_secondary.raise_()
        self.propertybrowser1.raise_()
        self.propertybrowser2.raise_()
        self.Delete_temporarily_button.raise_()
        self.Delete_permanently_button.raise_()
        self.Open_button.raise_()
        self.Decrypt_Button.raise_()
        self.Encrypt_button.raise_()
        self.Encrypt_All_button.raise_()
        self.navigate_back_button.raise_()
        self.navigate_next_button.raise_()
        self.settings_button.raise_()
        self.searchButton.raise_()
        self.appTitle.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.item_widget_primary.setSortingEnabled(True)
        __sortingEnabled = self.item_widget_primary.isSortingEnabled()
        self.item_widget_primary.setSortingEnabled(False)
        item = self.item_widget_primary.item(0)
        item.setText(_translate("MainWindow", "New Folder"))
        item = self.item_widget_primary.item(1)
        item.setText(_translate("MainWindow", "New Folder 2"))
        item = self.item_widget_primary.item(2)
        item.setText(_translate("MainWindow", "New Text Document"))
        item = self.item_widget_primary.item(3)
        item.setText(_translate("MainWindow", "New Text Document 2"))
        self.item_widget_primary.setSortingEnabled(__sortingEnabled)
        self.dir_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">C: &gt; Users &gt; Gobinda Das &gt; Desktop &gt;  </span></p></body></html>"))
        self.searchBar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Search Here"))
        __sortingEnabled = self.item_widget_secondary.isSortingEnabled()
        self.item_widget_secondary.setSortingEnabled(False)
        item = self.item_widget_secondary.item(0)
        item.setText(_translate("MainWindow", "This PC"))
        item = self.item_widget_secondary.item(1)
        item.setText(_translate("MainWindow", "C:"))
        item = self.item_widget_secondary.item(2)
        item.setText(_translate("MainWindow", "D:"))
        item = self.item_widget_secondary.item(3)
        item.setText(_translate("MainWindow", "E:"))
        item = self.item_widget_secondary.item(4)
        item.setText(_translate("MainWindow", "F:"))
        item = self.item_widget_secondary.item(5)
        item.setText(_translate("MainWindow", "G:"))
        self.item_widget_secondary.setSortingEnabled(__sortingEnabled)
        self.propertybrowser1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Size:   190038 bytes</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Type: Image</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Size on Disk: 190038</span></p></body></html>"))
        self.propertybrowser2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Size:   190038 bytes</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Type: Image</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Size on Disk: 190038</span></p></body></html>"))
        self.Delete_temporarily_button.setText(_translate("MainWindow", "Delete Temporarily"))
        self.Delete_permanently_button.setText(_translate("MainWindow", "Delete Permanently"))
        self.Open_button.setText(_translate("MainWindow", "Open"))
        self.Decrypt_Button.setText(_translate("MainWindow", "Decrypt"))
        self.Encrypt_button.setText(_translate("MainWindow", "Encrypt"))
        self.Encrypt_All_button.setText(_translate("MainWindow", "Encrypt Drive"))
        self.navigate_back_button.setText(_translate("MainWindow", "<<"))
        self.navigate_next_button.setText(_translate("MainWindow", ">>"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.appTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Pi File Explorer</span></p></body></html>"))
class mainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dir = 'C:\\Users\\Gobinda Das\\Desktop\\'
        self.__new_Path = None
        self.__clipboard = None
        self.password = 'Gunjan'
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        tt = self.__get_files_and_folders_in_dir()
        self.add_items_to_UI(tt)
        self.UI.item_widget_primary.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.UI.item_widget_primary.setContextMenuPolicy(Qt.CustomContextMenu)
        self.UI.item_widget_primary.customContextMenuRequested.connect(self.show_context_menu)
        self.UI.navigate_back_button.clicked.connect(self.remove_from_path)
        self.UI.Delete_temporarily_button.clicked.connect(self.delete_file)
        self.UI.Open_button.clicked.connect(self.open_file)
        self.UI.item_widget_primary.setCurrentRow(0)
        self.UI.item_widget_primary.clearSelection()
        # self.open_progressbar('App')
        # print(self.get_drive_partitions())
        self.UI.Encrypt_button.clicked.connect(self.encrypt_file)
        self.UI.Decrypt_Button.clicked.connect(self.decrypt_all)
    def open_progressbar(self, title):
        self.window = QMainWindow()
        self.progressbar = Ui_MainWindow2()
        self.progressbar.setupUi(self.window)
        flags = Qt.WindowMinimizeButtonHint | Qt.WindowTitleHint
        self.window.setWindowFlags(flags)
        self.window.setWindowTitle(str(title))
        self.progressbar.pushButton.clicked.connect(self.close_second_window)
        self.window.show()
    def get_drive_partitions(self):
        partitions = psutil.disk_partitions()
        drives = []
        cdrom_drive = ""
        external_drives = []
        # usb_devices = []

        for partition in partitions:
            if 'cdrom' in partition.opts or partition.fstype == '':
                if partition.mountpoint != '/':
                    cdrom_drive = partition.device
            else:
                if 'removable' in partition.opts:
                    external_drives.append(partition.device)
                else:
                    drives.append(partition.device)
        def get_usb_devices():
            usb_devices = []
            
            wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
            service = wmi.ConnectServer(".", "root\\cimv2")
            usb_query = "SELECT * FROM Win32_USBHub"
            usb_devices_data = service.ExecQuery(usb_query)
            
            for device in usb_devices_data:
                usb_devices.append(device.DeviceID)
            
            return usb_devices


        return drives, cdrom_drive, external_drives, get_usb_devices()
    def close_second_window(self):
        self.window.close()
    def handle_button_click(self):
        # Handle the button click in the second window
        print("Button clicked in the second window")
        
    def on_item_double_clicked(self, item):
        data = item.data(101)
        if data == str(False) and item.data(102) == 'file':
            self.open_file(item.data(100))
        elif data == str(True) and item.data(102) == 'file':
            file = open(item.data(100), 'rb').read()
            itemName = item.data(100).split("\\")[len(item.data(100).split("\\")) - 1]
            open(f'cache\\{itemName.replace(".encrypted", "")}', "wb").write(self.decrypt_data(zlib.decompress(file), self.password))
            os.startfile(f'cache\\{itemName.replace(".encrypted", "")}')
        elif item.data(102) == 'folder':
            self.dir = item.data(100)
            self.UI.item_widget_primary.clear()
            tt2 = self.__get_files_and_folders_in_dir()
            self.add_items_to_UI(tt2)
    def setDir(self, dir):
        self.UI.dir_browser.setText(str(dir))
    def show_drives(self):
        drives, cd, external = self.get_drive_partitions()
        for drive in drives:
            list_item = QListWidgetItem()
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap('Drive-icon.bmp'), QtGui.QIcon.Selected, QtGui.QIcon.On)
            list_item.setText(drive.replace('\\', ''))
            list_item.setIcon(icon)
            self.UI.item_widget_secondary.addItem(list_item)
        list_item = QListWidgetItem()
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap('CD-ROM.bmp'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        list_item.setText(cd.replace('\\', ''))
        list_item.setIcon(icon)
        self.UI.item_widget_secondary.addItem(list_item)
        for flash in external:
            list_item = QListWidgetItem()
            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap('Drive-icon.bmp'), QtGui.QIcon.Selected, QtGui.QIcon.On)
            list_item.setText(drive.replace('\\', ''))
            list_item.setIcon(icon)
            self.UI.item_widget_secondary.addItem(list_item)
    def show_context_menu(self, position):
        context_menu = QMenu(self)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        context_menu.addAction(open_action)

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_file)
        context_menu.addAction(delete_action)

        rename_action = QAction("Rename", self)
        rename_action.triggered.connect(self.rename_file)
        context_menu.addAction(rename_action)

        # Show the context menu at the requested position
        context_menu.exec_(self.UI.item_widget_primary.viewport().mapToGlobal(position))
    def show_dialog(self, text, title):
        message = "Are you sure you want to delete this item?"
        title = "Confirmation"
        style = ctypes.MessageBoxStyle.YES_NO | ctypes.MessageBoxStyle.ICON_QUESTION

        # Show the message box and get the user's choice
        result = ctypes.windll.user32.MessageBoxW(None, message, title, style)

    def open_file(self, file = None):
        if file == None or file == False:
            currentItem = self.UI.item_widget_primary.selectedItems()
            print(currentItem)
            if len(currentItem) != 0:
                os.startfile(currentItem[0].data(100))
            else:
                os.system('cscript delete.vbs')
        else:
            os.startfile(file)
    def delete_file(self):
        itemt = self.UI.item_widget_primary.selectedItems()
        if len(itemt) != 0:
            for item in itemt:
                file = item.data(100)
                send2trash(file)
        else:
            os.system('cscript delete.vbs')
    def delete_permanently(self):
        item = self.UI.item_widget_primary.selectedItems()
        if len(item) != 0:
            for itm in item:
                dta = itm.data(100)
                if os.path.isdir(dta):
                    shutil.rmtree(dta)
                elif os.path.isfile(dta):
                    os.remove(dta)
            self.UI.item_widget_primary.clear()
            self.add_items_to_UI(self.__get_files_and_folders_in_dir())
        else:
            os.system('cscript delete.vbs')
    def rename_file(self, text):
        item = self.UI.item_widget_primary.selectedItems()
        if len(item) != 0:
            components = item[0].data(100).split('\\')
            components = components[:-1]
            new_path = '\\'.join(components)
            os.rename(item[0].data(100), os.path.join(new_path, str(text)))
            self.UI.item_widget_primary.clear()
            self.add_items_to_UI(self.__get_files_and_folders_in_dir())
    def __generate_key_from_password(self, password, salt=b'salt', iterations=100_000, key_length=32):
        """
        Generates a key from the provided password using PBKDF2.
        """
        password = password.encode('utf-8')
        salt = salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=key_length,
            salt=salt,
            iterations=iterations
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
    def __write_conf(self, data):
        open('encryptionConfiguration.json', 'w').write(str(data).replace("'", '"'))
    def __read_conf(self):
        return json.loads(open('encryptionConfiguration.json', 'r').read())
    def encrypt_data(self, data, password):
        """
        Encrypts the provided data using the Fernet key.
        """
        key = self.__generate_key_from_password(password=password)
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data)
        return encrypted_data
    def decrypt_data(self, encrypted_data, password):
        """
        Decrypts the provided encrypted data using the Fernet key.
        """
        try:
            key = self.__generate_key_from_password(password=password)
            cipher_suite = Fernet(key)
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            return decrypted_data
        except Exception as e:
            if 'cryptography.fernet.InvalidToken' in str(e):
                return 'Invalid Password!'
    def encrypt_file(self, encrypt_subfolders = True):
        filet = self.UI.item_widget_primary.selectedItems()
        if len(filet) != 0:
            jsonData = self.__read_conf()
            filesEncrypted = self.__read_conf()["directoriesEncrypted"]
            for item in filet:
                file = item.data(100)
                if os.path.isdir(file):
                    self.encrypt_folder(file, encrypt_subfolders)
                elif os.path.isfile(file):
                    r = open(file, 'rb').read()
                    enc = self.encrypt_data(r, self.password)
                    enc = zlib.compress(enc)
                    open(file, 'wb').write(enc)
                    os.rename(file, f'{file}.encrypted')
                    filesEncrypted.append(f'{file}.encrypted')
                    jsonData["directoriesEncrypted"] = filesEncrypted
                    self.__write_conf(jsonData)
    def encrypt_chunks(self, data, password):
        key = self.__generate_key_from_password(password=password)
        cipher_suite = Fernet(key)
        chunk_size = 3 * 1024 * 1024
        data_length = len(data)
        chunk_length = len(data) / chunk_size
        iteration = 0
        if float(chunk_length) > int(chunk_length):
            chunk_length = int(chunk_length) + 1
        encrypted_data = b''
        for i in range(0, data_length, chunk_size):
            chunk = data[i:i + chunk_size]
            compressed_chunk = zlib.compress(chunk)
            encrypted_chunk = cipher_suite.encrypt(compressed_chunk)
            encrypted_data += encrypted_chunk + b' + '
            iteration = iteration + 1
            self.progressbar.firstProgressBar.setValue(round((iteration / chunk_length) * 100))
        cp = zlib.compress(encrypted_data)
        self.progressbar.progressBar.setValue(100)
        return cp

    def decrypt_chunks(self, encrypted_data, password):
        try:
            key = self.__generate_key_from_password(password=password)
            cipher_suite = Fernet(key)
            decrypted_data = b''
            splitted_data = zlib.decompress(encrypted_data).split(b' + ')
            total = len(splitted_data)
            iteration = 0
            for chunk in splitted_data:
                try:
                    decrypted_chunk = cipher_suite.decrypt(chunk)
                    self.progressbar.firstProgressBar.setValue(round((iteration / total) * 100))
                    decompressed_chunk = zlib.decompress(decrypted_chunk)
                    self.progressbar.progressBar_2.setValue(100)
                    decrypted_data += decompressed_chunk
                except Exception as e:
                    pass
                iteration = iteration + 1

            print("Decrypted Data Length:", len(decrypted_data))
            return decrypted_data
        except Exception as e:
            if 'cryptography.fernet.InvalidToken' in str(e):
                return 'Invalid Password!'
            else:
                print("Decryption Error:", e)

    
    def __get_files_and_folders_in_dir(self):
        items = []
        for item in os.listdir(self.dir):
            if '$' in item:
                pass
            elif os.path.isfile(os.path.join(self.dir, item)):
                if '.encrypted' in item:
                    items.append({'type':'file', 'name':item.replace('.encrypted', ''), 'encrypted':True})
                else:
                    items.append({'type':'file', 'name':item.replace('.encrypted', ''), 'encrypted':False})
            elif os.path.isdir(os.path.join(self.dir, item)):
                try:
                    if len(os.listdir(os.path.join(self.dir, item))) == 0:
                        items.append({'type':'folder', 'name':item.replace('.encrypted', ''), 'empty':True})
                    elif len(os.listdir(os.path.join(self.dir, item))) > 0:
                        items.append({'type':'folder', 'name':item.replace('.encrypted', ''), 'empty':False})
                except PermissionError:
                    items.append({'type':'folder', 'name':item.replace('.encrypted', ''), 'empty':False})
        return items
    def add_items_to_UI(self, items):
        # Icon paths
        folder_empty_icon_path = "FOLDER - EMPTY.png"
        folder_not_empty_icon_path = "FOLDER - FULL.png"
        file_e_icon_path = "file-icon.png"
        file_d_icon_path = "file-icon - Decrypted.png"
        # Add items to the QListWidget with the specified icon and name
        for item in items:
            name = item['name']
            item_type = item['type']

            list_item = QListWidgetItem()
            try:
                encrypted = item['encrypted']
            except:
                encrypted = False
            if item_type == 'file':
                icon_path = file_e_icon_path if encrypted else file_d_icon_path
            elif item_type == 'folder':
                empty = item['empty']
                icon_path = folder_empty_icon_path if empty else folder_not_empty_icon_path
            else:
                continue

            icon = QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Selected, QtGui.QIcon.On)
            list_item.setText(name)
            list_item.setIcon(icon)
            list_item.setData(100, os.path.join(self.dir, name))
            list_item.setData(101, f'{encrypted}')
            list_item.setData(102, item_type)
            self.UI.item_widget_primary.addItem(list_item)
    def add_to_path(self, folder):
        if os.path.exists(os.path.join(self.dir, folder)):
            self.dir = os.path.join(self.dir, folder)
            self.__get_files_and_folders_in_dir()
        else:
            return "Error: The folder doesn't exist!"
    def remove_from_path(self):
        folders = self.dir.split('\\')
        self.__new_path = '\\'.join(folders[:-1])
        self.dir = self.__new_path
        self.UI.item_widget_primary.clear()
        tt3 = self.__get_files_and_folders_in_dir()
        self.add_items_to_UI(tt3)
    def convert_size(self, size_in_bytes):
        size_in_kb = size_in_bytes / 1024
        size_in_mb = size_in_kb / 1024
        size_in_gb = size_in_mb / 1024

        if size_in_gb >= 1:
            return size_in_gb, "GB"
        elif size_in_mb >= 1:
            return size_in_mb, "MB"
        elif size_in_kb >= 1:
            return size_in_kb, "KB"
        else:
            return size_in_bytes, "bytes"
    def count_files(self, folder_path):
        file_count = 0

        for root, dirs, files in os.walk(folder_path):
            file_count += len(files)

        return file_count
    def find_space_needed(self, folder_path):
        file_new_sizes = []  # Array to store the sizes
        file_sizes = []
        total_files = self.count_files(folder_path)
        # Recursive function to process files in folder and subfolders
        
        def process_files(folder):
            a = 0
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    file_sizes.append(file_size)  
                    increase = file_size * 33.9124665762962 / 100  
                    new_size = file_size + increase  
                    file_new_sizes.append(new_size)
                    a = a + 1

        process_files(folder_path)
        total_size = sum(file_new_sizes)
        a, b = self.convert_size(total_size)
        c, d = self.convert_size(sum(file_sizes))
        return f"{c} {d.lower()}  >  {a} {b.lower()}"
    def copy_file(self, file_path):
        tt = file_path.split('\\')
        last_file = tt[-1]
        self.__clipboard = {'name': last_file,'content':open(file_path, 'rb').read()}
    def paste_file(self):
        open(os.path.join(self.dir, self.__clipboard["name"]), 'wb').write(self.__clipboard["content"])
    def cut_file(self, file_path):
        self.copy_file(file_path)
        os.remove(file_path)
    def encrypt_drive(self, drive):
        if self.password != None and drive != 'C:':
            jsonData = self.__read_conf()
            filesEncrypted = self.__read_conf()["directoriesEncrypted"]
            filesEncryptedInChunks = self.__read_conf()["filesEncryptedInChunks"]
            self.open_progressbar("Encrypting Files...")
            self.progressbar.processBrowser.setText("Encrypting Files...")
            self.progressbar.textBrowser_2.setText("Encrypting...")
            total = self.count_files(drive)
            iteration = 0
            tt = []
            for root, dirs, files in os.walk(drive):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.getsize(file_path) < 1024 * 1024 * 8:
                        self.progressbar.fileNameBrowser.setText(str(file))
                        self.progressbar.firstTextLabel.setText(f"Encrypting - {file}...")
                        normal_data = open(file_path, 'rb').read()
                        encrypted_data = self.encrypt_data(normal_data, self.password)
                        self.progressbar.firstProgressBar.setValue(100)
                        encrypted_data = zlib.compress(encrypted_data)
                        self.progressbar.progressBar.setValue(100)
                        with open(file_path, 'wb') as f:
                            f.write(encrypted_data)
                        os.rename(file_path, os.path.join(root, f'{file}.encrypted'))
                        filesEncrypted.append(f'{file_path}.encrypted')
                        iteration = iteration + 1
                        self.progressbar.firstProgressBar.setValue(0)
                        self.progressbar.progressBar.setValue(0)
                        self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))
                    else:
                        tt.append(file_path)
            for file in tt:
                self.progressbar.fileNameBrowser.setText(str(file.split('\\')[len(file.split('\\')) - 1]))
                ay = file.split('\\')[len(file.split('\\')) - 1]
                self.progressbar.firstTextLabel.setText(f"Encrypting - {ay}...")
                normal_data = open(file, 'rb').read()
                encrypted_data = self.encrypt_chunks(normal_data, self.password)
                with open(file, 'wb') as f:
                    f.write(encrypted_data)
                os.rename(file, os.path.join(root, f'{ay}.encrypted'))
                self.progressbar.firstProgressBar.setValue(0)
                self.progressbar.progressBar.setValue(0)
                iteration = iteration + 1
                self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))
                filesEncryptedInChunks.append(f'{file}.encrypted')

                    
            self.close_second_window()
            jsonData["directoriesEncrypted"] = filesEncrypted
            jsonData["filesEncryptedInChunks"] = filesEncryptedInChunks
            self.__write_conf(jsonData)
            return True
        else:
            return 'Error: System (C:) Drive cannot be encrypted! (TU)'
    def encrypt_folder(self, dir, encrypt_subfolders = False):
        if encrypt_subfolders:
            jsonData = self.__read_conf()
            filesEncrypted = self.__read_conf()["directoriesEncrypted"]
            filesEncryptedInChunks = self.__read_conf()["filesEncryptedInChunks"]
            self.open_progressbar("Encrypting Files...")
            self.progressbar.processBrowser.setText("Encrypting Files...")
            self.progressbar.textBrowser_2.setText("Encrypting...")
            total = self.count_files(dir)
            iteration = 0
            tt = []
            for root, dirs, files in os.walk(dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.getsize(file_path) < 1024 * 1024 * 8:
                        self.progressbar.fileNameBrowser.setText(str(file))
                        self.progressbar.firstTextLabel.setText(f"Encrypting - {file}...")
                        normal_data = open(file_path, 'rb').read()
                        encrypted_data = self.encrypt_data(normal_data, self.password)
                        self.progressbar.firstProgressBar.setValue(100)
                        encrypted_data = zlib.compress(encrypted_data)
                        self.progressbar.progressBar.setValue(100)
                        with open(file_path, 'wb') as f:
                            f.write(encrypted_data)
                        os.rename(file_path, os.path.join(root, f'{file}.encrypted'))
                        filesEncrypted.append(f'{file_path}.encrypted')
                        iteration = iteration + 1
                        self.progressbar.firstProgressBar.setValue(0)
                        self.progressbar.progressBar.setValue(0)
                        self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))
                    else:
                        tt.append(file_path)
            for file in tt:
                self.progressbar.fileNameBrowser.setText(str(file.split('\\')[len(file.split('\\')) - 1]))
                ay = file.split('\\')[len(file.split('\\')) - 1]
                self.progressbar.firstTextLabel.setText(f"Encrypting - {ay}...")
                normal_data = open(file, 'rb').read()
                encrypted_data = self.encrypt_chunks(normal_data, self.password)
                with open(file, 'wb') as f:
                    f.write(encrypted_data)
                os.rename(file, os.path.join(root, f'{ay}.encrypted'))
                self.progressbar.firstProgressBar.setValue(0)
                self.progressbar.progressBar.setValue(0)
                iteration = iteration + 1
                self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))
                filesEncryptedInChunks.append(f'{file}.encrypted')

                    
            self.close_second_window()
            jsonData["directoriesEncrypted"] = filesEncrypted
            jsonData["filesEncryptedInChunks"] = filesEncryptedInChunks
            self.__write_conf(jsonData)
            return True
        elif not encrypt_subfolders:
            jsonData = self.__read_conf()
            filesEncrypted = self.__read_conf()["directoriesEncrypted"]
            filesEncryptedInChunks = self.__read_conf()["filesEncryptedInChunks"]
            total = sum([1 for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))])
            iteration = 0
            self.open_progressbar("Encrypting Files...")
            self.progressbar.processBrowser.setText("Encrypting Files...")
            self.progressbar.textBrowser_2.setText("Encrypting...")
            tt = []
            for file in os.listdir(dir):
                file_path = os.path.join(dir, file)
                if os.path.isfile(file_path):
                    if os.path.getsize(file_path) < 1024 * 1024 * 8:
                        self.progressbar.fileNameBrowser.setText(str(file))
                        self.progressbar.firstTextLabel.setText(f"Encrypting - {file}...")
                        normal_data = open(file_path, 'rb').read()
                        encrypted_data = self.encrypt_data(normal_data, self.password)
                        self.progressbar.firstProgressBar.setValue(100)
                        encrypted_data = zlib.compress(encrypted_data)
                        self.progressbar.progressBar.setValue(100)
                        with open(file_path, 'wb') as f:
                            f.write(encrypted_data)
                        os.rename(file_path, f'{file_path}.encrypted')
                        filesEncrypted.append(f'{file_path}.encrypted')
                        iteration = iteration + 1
                        self.progressbar.firstProgressBar.setValue(0)
                        self.progressbar.progressBar.setValue(0)
                        self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))
                    else:
                        tt.append(file_path)
            for file in tt:
                self.progressbar.fileNameBrowser.setText(str(file.split('\\')[len(file.split('\\')) - 1]))
                ay = file.split('\\')[len(file.split('\\')) - 1]
                self.progressbar.firstTextLabel.setText(f"Encrypting - {ay}...")
                normal_data = open(file, 'rb').read()
                encrypted_data = self.encrypt_chunks(normal_data, self.password)
                self.progressbar.firstProgressBar.setValue(0)
                self.progressbar.progressBar.setValue(0)
                iteration = iteration + 1
                self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))
                filesEncryptedInChunks.append(file)
            self.close_second_window()
            jsonData["directoriesEncrypted"] = filesEncrypted
            jsonData["filesEncryptedInChunks"] = filesEncryptedInChunks
            self.__write_conf(jsonData)
            return True
    def decrypt_all(self):
        jsonData = self.__read_conf()
        dirs_encrypted = jsonData["directoriesEncrypted"]
        filesEncryptedInChunks = jsonData["filesEncryptedInChunks"]
        
        files_to_remove = []  # Create a list to store files that need to be removed
        total = len(dirs_encrypted) + len(filesEncryptedInChunks)
        iteration = 0
        f29 = []
        if len(dirs_encrypted) != 0:
            self.open_progressbar("Decrypting Files... ")
            self.progressbar.processBrowser.setText("Decrypting Files...")
            self.progressbar.textBrowser_2.setText("Decrypting...")
            self.progressbar.firstTextLabel.setText(f'Decompressing...')
            for file_path in dirs_encrypted:
                ay = file_path.split('\\')[len(file_path.split('\\')) - 1]
                self.progressbar.fileNameBrowser.setText(ay)
                self.progressbar.textBrowser.setText(f"Decrypting - {ay}...")
                encrypted_data = open(file_path, 'rb').read()
                encrypted_data = zlib.decompress(encrypted_data)
                decrypted_data = self.decrypt_data(encrypted_data, self.password)
                with open(file_path, 'wb') as f2:
                    f2.write(decrypted_data)
                files_to_remove.append(file_path)
                os.rename(file_path, file_path.replace('.encrypted', ''))
                iteration = iteration + 1
                self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))
            for file_path in filesEncryptedInChunks:
                encrypted_data = open(file_path, 'rb').read()
                decrypted_data = self.decrypt_chunks(encrypted_data, self.password)
                open(file_path, 'wb').write(decrypted_data)
                os.rename(file_path, file_path.replace('.encrypted', ''))
                f29.append(file_path)
                iteration = iteration + 1
                self.progressbar.progressBar_2.setValue(round((iteration / total) * 100))


            for file_path in files_to_remove:
                dirs_encrypted.remove(file_path)
            for fp in f29:
                filesEncryptedInChunks.remove(fp)

            jsonData["directoriesEncrypted"] = dirs_encrypted
            jsonData["filesEncryptedInChunks"] = filesEncryptedInChunks
            self.__write_conf(jsonData)
        else:
            return 'Error: No Files are encrypted yet! (TU)'


if __name__ == "__main__":
    app = QApplication([])

    # Create an instance of MyApplication
    my_app = mainClass()
    my_app.showMaximized()

    # Show the main window

    # Start the event loop
    app.exec_()