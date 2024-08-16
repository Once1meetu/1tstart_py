f = open("txt_task_3.2.txt", "r", encoding="utf-8")
#f.seek(0)
a=f.read(20)

#Определяет что за имя написано много раз в первых 20 символах
name = ""
for i in range(1,21):
    s = ""
    for j in range(i+1):
        s+=a[j]
    if(s[0:i] == a[i+1:2*i+1]):
        name=s
        break
f.close()

#Переписывает файл заново, добавляя имени окончание а
f = open("txt_task_3.2.txt", "w", encoding="utf-8")
for _ in range(10000):
    f.write(name+"а")
f.close()