import pprint

print("Учитывайте, что в одной папке с питоновским файлом должен быть файл 'Вопросы.txt', "
      "\nгде должны быть перечислены вопросы на каждой новой строке в виде '1. Вопрос. \\n'\n")

with open("Вопросы.txt", 'r', encoding="utf-8") as file:
    q = file.readlines()

print(f"Обнаружено {len(q)} вопросов. Вот они:")
for i in range(len(q)):
    q[i] = q[i][:-3]
    q[i] = q[i][:q[i].find(" ") - 1] + " -" + q[i][q[i].find(" "):]
    print(q[i])


def create_file():
    if input("Хотите создать файлы 'Предмет 1 - Вопрос 1 - Текст вопроса'?\n1. ДА\n2.НЕТ\n") == "1":
        name_file = input("Введите название файла, который будет использоваться в качестве шаблона.\n"
                          "Файл должен быть назван 'Предмет 1 - Вопрос.md'.\n"
                          "-> ")
        print()

        #name_file = "МПС 6 - Вопрос.md"

        with open(name_file, 'r', encoding="utf-8") as file:
            temp = file.read()

        for i in q:
            with open(f"{name_file[:-3]} {i}.md", "w", encoding="utf-8") as file:
                file.write(temp)

            print(f"Был создан и заполнен файл '{name_file[:-3]} {i}.md'")

def write():
    if input("Хотите дозаписать родительский файл 'Предмет 1 - Подготовка к экзамену'?\n1. ДА\n2.НЕТ\n") == "1":
        obj = input("Введите название предмета"
                    "Учитывайте, что все необходимые данные будут вставляться в конец файла: ")
        with open(f"{obj} - Подготовка к экзамену.md", 'a', encoding="utf-8") as file:
            
            for i in q:
                file.write(f"-  [[{obj} - Вопрос {i}|{i[i.find(" - ")+3:]}]]\n")
                

create_file()
write()
