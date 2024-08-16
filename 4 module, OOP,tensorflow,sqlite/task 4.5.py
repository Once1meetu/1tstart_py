import sqlite3
import turtle

db = sqlite3.connect("bd4_5")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT,
            password TEXT
)""")
db.commit()

user_login = input("login: ")
user_password = input("password: ")

sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
if(sql.fetchone() is None):
    sql.execute(f"INSERT INTO users VALUES (?, ?)", (user_login, user_password))
    db.commit()
else:
    print("Этот логин уже занят")
    for i in sql.execute("SELECT * FROM users"):
        print(i[0])


sql.execute("""CREATE TABLE IF NOT EXISTS data (x REAL, y REAL)""")
t = turtle.Turtle()
db.commit()

sql.execute("INSERT INTO data VALUES (?, ?)",(100,100))
sql.execute("INSERT INTO data VALUES (?, ?)",(100,-100))
sql.execute("INSERT INTO data VALUES (?, ?)",(-100,-100))
sql.execute("INSERT INTO data VALUES (?, ?)",(-100,100))
sql.execute("INSERT INTO data VALUES (?, ?)",(100,100))
db.commit()

sql.execute("SELECT x, y FROM data")
data = sql.fetchall()
print(data)
wd = turtle.Screen()

for x,y in data:
    c = wd.textinput("Выбор цвета", "Каким цветом рисовать?(red,green,blue,yellow,violet)")
    t.color(c)
    t.goto(x, y)
    ask = wd.textinput("Действие","Далее(ц) или Удалить(ы)")
    if (ask.lower()=='д'):
        continue
    elif (ask.lower()=='ы'):
        sql.execute(f"DELETE FROM data WHERE x={x}")
        t.undo()
        db.commit()

while True:
    len = turtle.Screen()
    x = len.numinput("x Len or -1", "x", minval= -10000, maxval= 10000)
    y = len.numinput("y Len or -1", "y", minval=-10000, maxval=10000)
    if (x==-1 or y==-1):
        break
    if (x!=None and y!=None):
        sql.execute("INSERT INTO data VALUES (?, ?)",(x, y))
        db.commit()
        t.goto(x, y)

turtle.done()
