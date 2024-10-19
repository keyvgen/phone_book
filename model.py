from collections import namedtuple

global_phone_book = {}
path_to_book = 'directory.txt'
separator = ';'
contact = namedtuple('contact', 'name, phone, comment')


def open_file():
    """Функция чтения информации из файла .txt"""

    with open(path_to_book, 'r', encoding='utf-8') as file:
        data = list(map(lambda x: x.strip().split(separator), file.readlines()))
        for cont in data:
            global_phone_book[int(cont[0])] = contact(*cont[1:])


def next_id():
    """Функция создания ID для контактов"""

    return max(global_phone_book) + 1


def save_file():
    """Запись информации в файл .txt"""

    data = []
    for cont_id, cont in global_phone_book.items():
        data.append(separator.join([str(cont_id), *cont]))
    with open(path_to_book, 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def add_contact(new_contact: list):
    """Функция добавления контакта"""

    cont = contact(*new_contact)
    global_phone_book[next_id()] = cont


def search_contact(cont_word: str):
    """Поиск контакта в глобальной переменной"""

    result = {}
    for i, cont in global_phone_book.items():
        for field in cont:
            if cont_word.lower() in field.lower():
                result[i] = cont
                break
    return result


def change_contact(cont_id: str, cont: list):
    """Изменение контакта"""

    new_contact = []
    current_contact = global_phone_book[int(cont_id)]
    for i in range(len(cont)):
        new_contact.append(cont[i] if cont[i] else current_contact[i])
    global_phone_book[int(cont_id)] = contact(*new_contact)
    return new_contact[0]


def delete_contact(cont_id: str):
    """Удаление контакта"""

    cont = global_phone_book.pop(int(cont_id))
    return cont.name
