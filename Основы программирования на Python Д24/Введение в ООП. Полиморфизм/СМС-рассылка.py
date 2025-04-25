class Person:
    def __init__(self, name: str, surname: str, father_name: str, phones: dict[str, int]):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return f'{self.father_name} {self.name} {self.surname}'

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.surname}! Примите участие в нашем '\
                'беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name: str, company_type: str, phones: dict[str, int], *employees):
        self.name = name
        self.company_type = company_type
        self.phones = phones
        self.employees = employees

    def get_phone(self):
        if self.phones.get('contact'):
            return self.phones.get('contact')
        for employee in self.employees:
            if employee.get_work_phone():
                return employee.get_work_phone()

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! Примите участие в нашем '\
               f'беспроигрышном конкурсе для {self.company_type}'


def send_sms(*recipients):
    for recipient in recipients:
        recipient: Person | Company
        if recipient.get_phone():
            print(f'Отправлено СМС на номер {recipient.get_phone()} с текстом: {recipient.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {recipient.get_name()}')