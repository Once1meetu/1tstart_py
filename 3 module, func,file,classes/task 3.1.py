import turtle

def drawsquare(sidelenth):
    for _ in range(4):
        turtle.forward(sidelenth)
        turtle.right(90)

def introduse():
    fio = input("Enter your full name\n")
    while True:
        mail = input("Enter your e-mail\n")
        if mail.find('@')>=0 and mail.find('.')>=0:
            break
    while True:
        phonenumber = input("Enter your phone number\n")
        if phonenumber.isdigit():
            break
    return [fio, mail, phonenumber]

people = []
while True:
    people.append(introduse())
    n = float(input("Enter size of square, 0 to finish\n"))
    if n==0:
        break;
    drawsquare(n)
print(people)
turtle.done()