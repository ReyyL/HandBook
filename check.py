class Check:

    def __init__(self, str):
        try:
            info = str.split(' ')
            self.name = info[0]
            self.last_name = info[1]
            self.phone_number = info[2]
            self.city = info[3]
            self.email = info[4]
        except Exception:
            print('Неверный ввод. Повторите попытку.', end='\n')

    def note_is_right(self):
        try:
            name = all(map(str.isalpha, self.name)) and self.name[0].isupper()
            last_name = all(map(str.isalpha, self.last_name)) and self.last_name[0].isupper()
            city = all(map(str.isalpha, self.city)) and self.city[0].isupper()
            number = all(map(str.isdigit, self.phone_number)) and len(self.phone_number) == 11 \
                     and (self.phone_number[0] == '7' or self.phone_number[0] == '8')
            email = '@' in self.email and '.' in self.email
        except Exception:
            print('Неверный ввод. Повторите попытку.', end='\n')
        return name and last_name and city and number and email

    def check_to_str(self):
        return '{} {} {} {} {}'.format(self.name, self.last_name, self.phone_number, self.city, self.email)
