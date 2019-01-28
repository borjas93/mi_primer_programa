def in_range(number, list):

    if number > list[0] and number < list[len(list)-1]:

        print(True)

    else:

        print(False)

def sort_number(number_a, number_b):

    if number_a < number_b:

        smallest = number_a
        biggest = number_b

    else:

        smallest = number_b
        biggest = number_a

    return smallest, biggest

user_number = float(input('\nIntroduce un numero: \n'))
a = int(input('Primer numero: \n'))
b = int(input('Segundo numero: \n'))

range_number = sort_number(a, b)
user_list = range(sort_number.smallest(), sort_number.biggest())

in_range(user_number, user_list)

