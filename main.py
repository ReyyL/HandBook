import os
from notesActions import notesActions

def main():
    answer = 0
    while True:
        answer = commands()
        if answer == -1:
            break


def commands():
    print('Список команд:', end='\n')
    print('1: Создать справочник', end='\n')
    print('2: Изменить текущий справочник', end='\n')
    print('3: Добавить запись', end='\n')
    print('4: Изменить запись', end='\n')
    print('5: Найти запись', end='\n')
    print('6: Удалить запись', end='\n')
    print('7: Закрыть справочник', end='\n')
    number = int(input())
    if number == 1:
        create()
    elif number == 2:
        change_current_handbook()
    elif number == 3:
        current_handbook.add_note()
    elif number == 4:
        current_handbook.change_note()
    elif number == 5:
        current_handbook.find_note()
    elif number == 6:
        current_handbook.delete_note()
    elif number == 7:
        return -1
    else:
        print('Неверный ввод. Повторите попытку', end='\n')
        return 1


def create():
    global current_handbook
    handbook_name = input("Введите имя справочника: ")
    if (handbook_name.isalpha() or handbook_name.isdigit()) and len(handbook_name) > 3:
        current_handbook = notesActions(handbook_name)
        handbooks[handbook_name] = current_handbook
        handbook = open(handbook_name + ".txt", "a")
        handbook.close()
        print('Справочник создан.', end='\n')
    else:
        print('Введенное имя содержит неверные символы, либо имеет недостаточную длину')


def change_current_handbook():
    global current_handbook
    handbook_name = input("Введите имя справочника: ")
    if os.path.exists(os.path.abspath(handbook_name + '.txt')):
        current_handbook = handbooks[handbook_name]
        print('Текущий справочник изменён на ', handbook_name, '.', end='\n')
    else:
        print('Справочника с таким именем не существует. Создать его? (yes/no)', end='\n')
        answer = input()
        if answer == 'yes':
            if (handbook_name.isalpha() or handbook_name.isdigit()) and len(handbook_name) > 3:
                current_handbook = notesActions(handbook_name)
                handbooks[handbook_name] = current_handbook
                handbook = open(handbook_name + ".txt", "a")
                handbook.close()
                print('Справочник создан.', end='\n')
            else:
                print('Введенное имя содержит неверные символы, либо имеет недостаточную длину')
        if answer == 'no':
            return

handbooks = dict()
current_handbook = notesActions('')
handbooks[''] = current_handbook

for file in os.listdir(os.getcwd()):
    if file.endswith('.txt'):
        handbooks[file[:-4]] = notesActions(file[:-4])
main()