import sys
from datetime import date
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector as mysql

todaydate = date.today().strftime("%B %d, %Y")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('mood tracker')
        self.setFixedWidth(1080)
        self.setFixedHeight(720)
        self.MainUI()
        self.show()
    
    def onclickbutton(self):
        self.newwindow = CreateDBWindow()
        self.newwindow.show()
        self.newwindow.move(self.pos())
    
    def MainUI(self):
        heading = QLabel('home',self)
        heading.move(50,20)
        heading.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')
        heading.show()
        
        today = QLabel('today:',self)
        today.move(50,90)
        today.setStyleSheet('font-size: 24px; font-weight: thin; font-family: Verdana, sans-serif;')
        today.show()

        date = QLabel(todaydate,self)
        date.move(145,90)
        date.setStyleSheet('font-size: 24px; font-weight: thin; font-family: Verdana, sans-serif;')
        date.show()
        
        imagelabel = QLabel(self)
        image = QPixmap('House.png')
        nimage = image.scaled(QSize(120,120))
        imagelabel.setPixmap(nimage)
        imagelabel.move(900,20)
        imagelabel.show()

        mood = QLabel('good',self)
        mood.move(50,200)
        mood.setStyleSheet('font-size: 48px; color: #219653; font-weight: bold; font-family: Verdana,sans-serif;')
        mood.show()
        
        moodLabel = QLabel('current mood',self)
        moodLabel.move(50,270)
        moodLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        moodLabel.show()
        
        ads = QLabel('7.6',self)
        ads.move(400,200)
        ads.setStyleSheet('font-size: 48px; color: #DCAC00; font-weight: bold; font-family: Verdana,sans-serif;')
        ads.show()
        
        adsLabel = QLabel('average day score',self)
        adsLabel.move(400,270)
        adsLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        adsLabel.show()
        
        totentries = QLabel('123',self)
        totentries.move(800,200)
        totentries.setStyleSheet('font-size: 48px; font-weight: bold; font-family: Verdana,sans-serif;')
        totentries.show()

        totentriesLabel = QLabel('total entries',self)
        totentriesLabel.move(800,270)
        totentriesLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
        totentriesLabel.show()
        
        actions = QLabel('actions',self)
        actions.move(50,370)
        actions.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')
        actions.show()

        actionsButtons=QScrollArea(self)
        actionsButtons.move(50,440)
        actionsButtons.resize(980,150)
        actionsButtons.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        actionsButtons.setWidgetResizable(True)
        actionsButtons.show()
        
        actionsBox = QGridLayout()
        creDB = QPushButton('create database',self)
        creDB.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        creDB.clicked.connect(self.onclickbutton)
        creDB.show()

        addEn = QPushButton('add an entry',self)
        addEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        addEn.show()
        
        editEn = QPushButton('edit an entry',self)
        editEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        editEn.show()
        
        viewEn = QPushButton('view entries',self)
        viewEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        viewEn.show()
        
        delEn = QPushButton('delete an entry',self)
        delEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        delEn.show()
        
        showSumm = QPushButton('show summary',self)
        showSumm.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
        showSumm.show()
        
        actionsBox.addWidget(creDB,0,0)
        actionsBox.addWidget(addEn,0,1)
        actionsBox.addWidget(editEn,0,2)
        actionsBox.addWidget(viewEn,1,0)
        actionsBox.addWidget(delEn,1,1)
        actionsBox.addWidget(showSumm,1,2)

        new = QWidget()
        new.setLayout(actionsBox)
        actionsButtons.setWidget(new)
        actionsButtons.show()
        
        copyrightText = QLabel('© mood tracker 2023',self)
        copyrightText.move(480,690)
        copyrightText.setStyleSheet('font-weight:thin;font-family: Verdana,sans-serif; font-size: 16px;')
        copyrightText.show()

class CreateDBWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('mood tracker')
        self.setFixedWidth(1080)
        self.setFixedHeight(720)
        self.MainUI()
        self.show()
    def MainUI(self):
        hi = QLabel('hi there, it works!',self)
        hi.show()

app = QApplication([])
app.setStyle('Fusion')
mw = MainWindow()
app.exec_()