import pickle

from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT,
                ACTION_REMOVE_CONTACT,
                ACTION_FIND_CONTACT,
                ACTION_EXPORT_CONTACT,
                ACTION_EXIT]


class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\nAñadir contacto\n")
    contact = Contact(name = input('Nombre: '), number = input('\nNúmero: '), email = input('\nEmail: '))
    contacts.append(contact)
    print("\nSe ha añadido el contacto {} correctamente\n".format(contact.name))
    sleep(1)


def remove_contact(contacts):
    print('\n\nBorrar contacto\n')
    contact_to_remove = find_contact(contacts)
    try:
        confirm = input('Vas a borrar a {}. ¿Estás seguro? S/N '.format(contact_to_remove.name)).capitalize()
        if confirm == 'S':
            print('\nEl contacto {} ha sido borrado con éxito.\n'.format(contact_to_remove.name).capitalize())
            del contact_to_remove.name

        else:
            remove_contact(contacts)

        sleep(2)
    except AttributeError:
        return


def find_contact(contacts):
    print("\nBuscar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        try:
            while search_term not in contact.name:
                search_term = input('Introduce el nombre del contacto o parte de el: ')

            if search_term in contact.name:
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact.name))
                contact_indexes.append(contact_counter)
                contact_counter += 1
        except AttributeError:
            print('\nLista de contactos vacía.\n')
            return
    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    choosen = found_contacts[contact_index]
    print("\nInformación sobre {}\n".format(choosen.name))
    print("Nombre: {}, Telefono: {}, Email: {}\n\n".format(choosen.name, choosen.number, choosen.email))
    sleep(2)
    return choosen

def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()
