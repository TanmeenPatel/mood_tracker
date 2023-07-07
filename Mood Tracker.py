import sys
from datetime import date
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector as mysql

app = QApplication([])
app.setStyle('Fusion')
win = QWidget()
win.setWindowTitle('mood tracker')
win.setFixedWidth(1080)
win.setFixedHeight(720)

def createDB():
    heading1.hide()
    today.hide()
    date.hide()
    imagelabel1.hide()
    mood.hide()
    moodLabel.hide()
    ads.hide()
    adsLabel.hide()
    totentries.hide()
    totentriesLabel.hide()
    actions.hide()
    actionsButtons.hide()
    heading2.show()
    imagelabel2.show()
    hostLabel.show()
    host.show()
    userLabel.show()
    user.show()
    passwordLabel.show()
    password.show()
    databaseLabel.show()
    database.show()
    createDBbutton.show()
    backbutton.show()

heading1 = QLabel('home',parent=win)
heading1.move(50,20)
heading1.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')

today = QLabel('today:',parent=win)
today.move(50,90)
today.setStyleSheet('font-size: 24px; font-weight: thin; font-family: Verdana, sans-serif;')

todaydate = date.today().strftime("%B %d, %Y")
date = QLabel(todaydate,parent=win)
date.move(145,90)
date.setStyleSheet('font-size: 24px; font-weight: thin; font-family: Verdana, sans-serif;')

imagelabel1 = QLabel(parent=win)
image1 = QPixmap('House.png')
nimage1 = image1.scaled(QSize(120,120))
imagelabel1.setPixmap(nimage1)
imagelabel1.move(900,20)

mood = QLabel('good',parent=win)
mood.move(50,200)
mood.setStyleSheet('font-size: 48px; color: #219653; font-weight: bold; font-family: Verdana,sans-serif;')

moodLabel = QLabel('current mood',parent=win)
moodLabel.move(50,270)
moodLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')

ads = QLabel('7.6',parent=win)
ads.move(400,200)
ads.setStyleSheet('font-size: 48px; color: #DCAC00; font-weight: bold; font-family: Verdana,sans-serif;')

adsLabel = QLabel('average day score',parent=win)
adsLabel.move(400,270)
adsLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')

totentries = QLabel('123',parent=win)
totentries.move(800,200)
totentries.setStyleSheet('font-size: 48px; font-weight: bold; font-family: Verdana,sans-serif;')

totentriesLabel = QLabel('total entries',parent=win)
totentriesLabel.move(800,270)
totentriesLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')

actions = QLabel('actions',parent=win)
actions.move(50,370)
actions.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')

actionsButtons=QScrollArea(parent=win)
actionsButtons.move(50,440)
actionsButtons.resize(980,150)
actionsButtons.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
actionsButtons.setWidgetResizable(True)

actionsBox = QGridLayout()
creDB = QPushButton('create database',parent=win)
creDB.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
creDB.clicked.connect(createDB)

addEn = QPushButton('add an entry',parent=win)
addEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')

editEn = QPushButton('edit an entry',parent=win)
editEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')

viewEn = QPushButton('view entries',parent=win)
viewEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')

delEn = QPushButton('delete an entry',parent=win)
delEn.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')

showSumm = QPushButton('show summary',parent=win)
showSumm.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')

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

heading2 = QLabel('create database',parent=win)
heading2.move(50,20)
heading2.setStyleSheet('font-size: 56px; font-family: Times New Roman, serif')
heading2.hide()

imagelabel2 = QLabel(parent=win)
image2 = QPixmap('Hammer.png')
nimage2 = image2.scaled(QSize(120,120))
imagelabel2.setPixmap(nimage2)
imagelabel2.move(900,20)
imagelabel2.hide()

hostLabel = QLabel('host: ',parent=win)
hostLabel.move(50,150)
hostLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
hostLabel.hide()

host = QLineEdit(parent=win)
host.move(190,150)
host.setFixedWidth(500)
host.setFixedHeight(40)
host.setStyleSheet('font-size: 20px')
host.hide()

userLabel = QLabel('user: ',parent=win)
userLabel.move(50,230)
userLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
userLabel.hide()

user = QLineEdit(parent=win)
user.move(190,230)
user.setFixedWidth(500)
user.setFixedHeight(40)
user.setStyleSheet('font-size: 20px')
user.hide()

passwordLabel = QLabel('password: ',parent=win)
passwordLabel.move(50,310)
passwordLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
passwordLabel.hide()

password = QLineEdit(parent=win)
password.move(190,310)
password.setFixedWidth(500)
password.setFixedHeight(40)
password.setStyleSheet('font-size: 20px')
password.hide()

databaseLabel = QLabel('database: ',parent=win)
databaseLabel.move(50,390)
databaseLabel.setStyleSheet('font-size: 24px; font-family: Verdana,sans-serif;')
databaseLabel.hide()

database = QLineEdit(parent=win)
database.move(190,390)
database.setFixedWidth(500)
database.setFixedHeight(40)
database.setStyleSheet('font-size: 20px')
database.hide()

createDBbutton = QPushButton('create database',parent=win)
createDBbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
createDBbutton.move(50,480)
createDBbutton.hide()

backbutton = QPushButton('back to home',parent=win)
backbutton.setStyleSheet('padding: 5px 15px; background-color: #C5C5C5; font-style:italic;font-family: Verdana,sans-serif; font-size: 20px;')
backbutton.move(300,480)
backbutton.hide()

copyrightText = QLabel('© mood tracker 2023',parent=win)
copyrightText.move(480,690)
copyrightText.setStyleSheet('font-weight:thin;font-family: Verdana,sans-serif; font-size: 16px;')

win.show()
sys.exit(app.exec())