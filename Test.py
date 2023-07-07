import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector as mysql

con = mysql.connect(host='localhost', user= 'root', password = 'x8_5!43', database='ComputerProject')
cur = con.cursor()

app = QApplication([])
app.setStyle('Fusion')
win = QWidget()
win.setWindowTitle('Test')
win.setStyleSheet('background-color: #bbb2e9;')

def button_clicked():
    cur.execute("create table testtable(test varchar(10))")
    
def submit_clicked():
    x = textArea.text()
    print(x)
    cur.execute('insert into testtable values("{}");'.format(textArea.text()))
    con.commit()

title = QLabel('''<h1>HELLO WORLD</h1>''', parent=win)
title.move(600,300)
title.setStyleSheet('color: pink')

button = QPushButton('Create Table',parent=win)
button.clicked.connect(button_clicked)
button.setStyleSheet('background-color: cyan; padding: 15px')
button.move(600,370)

imagelabel = QLabel(parent=win)
image = QPixmap('image.png')
nimage = image.scaled(QSize(100,100))
imagelabel.setPixmap(nimage)
imagelabel.move(600,420)
# imagelabel.setStyleSheet('width:50px,height:50px')

textArea = QLineEdit(parent=win)
textArea.move(600,540)
textArea.setFixedWidth(150)
textArea.setFixedHeight(75)

submit = QPushButton('Submit',parent=win)
submit.move(600,625)
submit.clicked.connect(submit_clicked)

layout = QGridLayout()
layout.addWidget(QLabel('hello',parent=win), 0, 0)
layout.addWidget(QLabel('how',parent=win), 0, 1)
layout.addWidget(QLabel('r',parent=win), 1, 0)
layout.addWidget(QLabel('u',parent=win), 1, 1)
lyt = QWidget()
lyt.setLayout(layout)
lyt.move(600,700)
lyt.show()

win.show()
sys.exit(app.exec())