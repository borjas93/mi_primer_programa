import datetime as time

today = time.date.today()

five_da = today - time.timedelta(days = 5)

print(five_da)

dias_semana = {'0': 'Lunes',
               '1': 'Martes',
               '2': 'Miercoles',
               '3': 'Jueves',
               '4': 'Viernes',
               '5': 'Sabado',
               '6': 'Domingo'}

day = int(input('\n¿Que dia es tu cumpleaños? '))
month = int(input('\n¿De que mes? '))
year = int(input('\n¿De que año? '))

birthday = time.date(year = year, month = month, day = day)
remaining_time = birthday - today
print('')
print('Faltan {} dias para tu cumpleaños.'.format(
    remaining_time))
print('')
print('Tu cumpleaños cae en {}.'.format(
    dias_semana[str(birthday.weekday())]))