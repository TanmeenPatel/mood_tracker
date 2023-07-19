# x = ""
# def checkLoggedIn():
#     if x == "":
#         print("nope")
#         return "nope"
# y = checkLoggedIn()
# if y == "nope":
#     print('it should work then')

# from datetime import date
# lineeditdate = date.today().strftime("%Y-%m-%d")
# print(lineeditdate)

import mysql.connector as mysql
con = mysql.connect(host='localhost', user='root', password='x8_5!43', database="moodtracker")
cur = con.cursor()
cur.execute("select mood from mood limit 1")
moods = cur.fetchone()
currentmood = moods[0]
print(currentmood)