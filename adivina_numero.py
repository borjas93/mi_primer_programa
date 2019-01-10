attempts = 0
initial_attempts = 5
remaining_attempts = initial_attempts
number_to_guess = 2

while attempts != initial_attempts:

    attempts += 1
    remaining_attempts -= 1
    user_number = int(input('Adivina un numero: '))

    if user_number != number_to_guess:

        if remaining_attempts > 1:
            print("Te quedan {} intentos." .format(remaining_attempts))
        elif remaining_attempts == 1:
            print("Te quedan {} intento.".format(remaining_attempts))
        else:
            print('Ya no te quedan intentos.')
            break
        print('Prueba otra vez')

    else:
        print('¡Has acertado!')
        break