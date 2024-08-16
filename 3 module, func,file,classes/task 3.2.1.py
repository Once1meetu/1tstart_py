#Создаёт файл, где имя пользователя записано 10к раз
f = open("txt_task_3.2.txt", "w", encoding="utf-8")
name=input("Enter your name(with uppercate letter)\n")
for _ in range(10000):
    f.write(name)
f.close()
