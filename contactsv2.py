import pickle
from tkinter import *
from tkinter import ttk
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


def tk_list(contacts, name, phone, email, contact_list_frame):

    contact = add_contact(contacts, name, phone, email)
    cols, row = contact_list_frame.grid_size()
    ttk.Label(contact_list_frame, text=contact.name).grid(column=1, row=row, sticky=(W,N,E,S))
    ttk.Label(contact_list_frame, text=contact.email).grid(column=2, row=row, sticky=(W,N,E,S))
    ttk.Label(contact_list_frame, text=contact.number).grid(column=3, row=row, sticky=(W,N,E,S))


def add_contact(contacts, name, phone, email):
    contact = Contact(
        name = name,
        number = phone,
        email = email)
    contacts.append(contact)

    print("\nSe ha añadido el contacto {} correctamente\n".format(contact.name))

    return contact


def ask_contact(contacts):
    print("\nAñadir contacto\n")
    contact = add_contact(contacts,
                          input('Nombre: '),
                          input('\nNúmero: '),
                          input('\nEmail: '))
    print("\nSe ha añadido el contacto {} correctamente\n".format(contact.name))
    return contact


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


def exit_program(contacts):
    save_contacts(contacts)
    exit()


def init_tk_list(contacts, contact_list_frame):
    for contact in contacts:
        cols, row = contact_list_frame.grid_size()
        ttk.Label(contact_list_frame, text=contact.name).grid(column=1, row=row, sticky=(W,N,E,S))
        ttk.Label(contact_list_frame, text=contact.email).grid(column=2, row=row, sticky=(W,N,E,S))
        ttk.Label(contact_list_frame, text=contact.number).grid(column=3, row=row, sticky=(W,N,E,S))


def main():

    contacts = load_contacts()

    root = Tk()
    root.title('Agenda de teléfonos')

    add_contact_frame = ttk.Frame(root, padding="3 3 3 3")
    add_contact_frame.grid(column=0, row=0)

    contact_list_frame = ttk.Frame(root, padding="3 3 3 3")
    contact_list_frame.grid(column=0, row=1)

    ttk.Label(add_contact_frame, text='Nombre:').grid(column=1, row=1, sticky = W)
    ttk.Label(add_contact_frame, text='Email:').grid(column=2, row=1, sticky = W)
    ttk.Label(add_contact_frame, text='Número:').grid(column=3, row=1, sticky = W)

    name = StringVar()
    email = StringVar()
    number = StringVar()

    name_entry = ttk.Entry(add_contact_frame, width=15, textvariable=name)
    name_entry.grid(column=1, row=2)

    email_entry = ttk.Entry(add_contact_frame, width=15, textvariable=email)
    email_entry.grid(column=2, row=2)

    number_entry = ttk.Entry(add_contact_frame, width=15, textvariable=number)
    number_entry.grid(column=3, row=2)

    ttk.Button(add_contact_frame,
               text="Añadir",
               command=lambda: tk_list(contacts,
                                       name.get(),
                                       number.get(),
                                       email.get(),
                                       contact_list_frame)
               ).grid(column=1, row=3, sticky=(W,N,E,S))

    ttk.Button(add_contact_frame,
               text="Guardar y salir",
               command=lambda: exit_program(contacts)
               ).grid(column=3, row=3, sticky=(W, N, E, S))

    ttk.Label(contact_list_frame, text='Nombre:').grid(column=1, row=1, sticky=(W,N,E,S))
    ttk.Label(contact_list_frame, text='Email:').grid(column=2, row=1, sticky=(W,N,E,S))
    ttk.Label(contact_list_frame, text='Número:').grid(column=3, row=1, sticky=(W,N,E,S))

    init_tk_list(contacts, contact_list_frame)

    for child in add_contact_frame.winfo_children():
        child.grid_configure(padx=10, pady=2)
    for child in contact_list_frame.winfo_children():
        child.grid_configure(padx=30, pady=2)

    root.mainloop()

    exit_program(contacts)


if __name__ == "__main__":
        main()






