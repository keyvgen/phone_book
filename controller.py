import view
import model
import text_file


def start_book():
    """Функция для выбора пунктов меню"""

    start_bottom = True
    while start_bottom:
        view.show_menu()
        user_choice = view.choice_menu()
        match user_choice:
            case 1:
                model.open_file()
                view.print_message(text_file.open_directory_success)
            case 2:
                model.save_file()
                view.print_message(text_file.save_directory_success)
            case 3:
                view.show_all_contacts(model.global_phone_book)
            case 4:
                contact = view.input_contact(text_file.new_contact_create)
                model.add_contact(contact)
                view.print_message(text_file.add_contact_success(contact[0]))
            case 5:
                search_word = view.data_input(text_file.search_word)
                result = model.search_contact(search_word)
                view.print_message(result)
            case 6:
                changed_id = view.data_input(text_file.input_changed_id)
                changed_contact = view.input_contact(text_file.change_contact)
                name = model.change_contact(changed_id, changed_contact)
                view.print_message(text_file.change_contact_success(name))
            case 7:
                cont_id = view.data_input(text_file.input_delete_id)
                name = model.delete_contact(cont_id)
                view.print_message(text_file.delete_contact_success(name))
            case 8:
                view.print_message(text_file.good_bye)
                start_bottom = False
