import text_file


def data_input(msg: str):
    """Функция для ввода информации"""

    return input(msg)


def input_contact(msg):
    """Ввод информации для создания контакта или его изменения"""

    data = []
    for item in msg:
        data.append(data_input(item))
    return data


def choice_menu():
    """Функция выбора пункта меню"""

    bottom = True
    while bottom:
        menu_item = data_input(text_file.menu_item_choice)
        if menu_item.isdigit() and 0 < int(menu_item) < len(text_file.main_menu):
            return int(menu_item)
        print(text_file.menu_item_error)


def show_menu():
    """Функция для отображения пунктов меню"""

    for i, item in enumerate(text_file.main_menu):
        if not i:
            print(item)
        else:
            print(f'{i}- {item}')


def print_message(msg: str):
    """Печать сообщений при работе с пунктами меню"""

    print('\n' + text_file.message_separator * len(msg))
    print(msg)
    print(text_file.message_separator * len(msg) + '\n')


def show_all_contacts(book: dict, column_size: int = 30):
    """Печать телефонного справочника"""

    print('\n' + text_file.message_separator * (3 + column_size * 3))
    for i, contact in book.items():
        print(f'{i: >3} {contact.name: <{column_size}}'
              f' {contact.phone: <{column_size}} {contact.comment}')
    print(text_file.message_separator * (3 + column_size * 3) + '\n')
