from check import Check

class notesActions:

    def __init__(self, name):
        self.name = name


    def add_note(self):
        note_name = Check(input('Введите через пробел имя, фамилию, номер телефона(без плюса), город и e-mail:'))
        if note_name.note_is_right():
            handbook = open(self.name + '.txt', 'r')
            notes = handbook.read()
            handbook.close()
            if note_name.check_to_str() in notes:
                print('Такая запись уже существует.', end='\n')
                return
            if note_name.phone_number in notes:
                print('Запись с таким номером уже существует.', end='\n')
                return
            if note_name.name and note_name.last_name in notes:
                print('Запись c такими именем и фамилией уже существует.', end='\n')
                return
            if note_name.email in notes:
                print('Запись с таким e-mail уже существует.', end='\n')
                return
            handbook = open(self.name + '.txt', 'a')
            handbook.write(note_name.check_to_str() + '\n')
            handbook.close()
            print('Запись добавлена.', end='\n')
        else:
            print('Неверный ввод. Повторите попытку.', end='\n')


    def change_note(self):
        number = input('Введите номер телефона записи, которую надо изменить')
        handbook = open(self.name + '.txt', 'r')
        notes = handbook.read()
        handbook.seek(0)
        if number in notes:
            print('Введите новое значение:', end='\n')
            new_note_name = Check(input())
            if new_note_name.note_is_right():
                notes = handbook.readlines()
                handbook.close()
                handbook = open(self.name + '.txt', 'w')
                for note in notes:
                    if number in note:
                        handbook.write(new_note_name + '\n')
                    else:
                        handbook.write(note + '\n')
                print('Значение изменено.', end='\n')
            return
        print('Такой записи не существует.', end='\b')


    def find_note(self):
        searching_param = input('Введите один из параметров для поиска:')
        handbook = open(self.name + '.txt', 'r')
        notes = handbook.readlines()
        counter = 0
        for note in notes:
            if searching_param in note:
                print(note, end='\n')
                counter += 1
        print('Найдено записей: ', counter, end='\n')


    def delete_note(self):
        is_deleted = False
        email = input('Введите e-mail удаляемой записи:')
        handbook = open(self.name + '.txt', 'r')
        notes = handbook.readlines()
        handbook.close()
        handbook = open(self.name + '.txt', 'w')
        for note in notes:
            if email in note:
                is_deleted = True
            else:
                handbook.write(note)
        handbook.close()
        if is_deleted:
            print('Запись удалена.', end='\n')
        else:
            print('Записи с таким e-mail не существует.', end='\n')
