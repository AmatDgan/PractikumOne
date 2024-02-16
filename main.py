import math

print('Hello, Python!')

print('Привет, Python!')
print('Hello, Python!')
print('Bonjour Python!')
print('Hej, Python!')
print('Hola, Python!')

print('Привет')
print('Python!')

print('(\___/)')
print("(='.'=)")
print('(")_(")')

print('Привет, Python!', 'Hello, Python!', 'Bonjour Python!', 'Hej, Python!', 'Hola, Python!', sep='\n')

x = str(input('Как вас зовут? '))
print(f'Здравствуйте, {x}')

x = str(input('Как вас зовут? '))
print(f'Здравствуйте, {x}')
y = str(input('Что вам нравится? '))
print(f'Отлично! {y} - хорошее увлечение.')

x = str(input('Login: '))
y = str(input('Password: '))
z = str(input('New password: '))
print(f'User {x} has changed the password to {z}')

print('Введите плей-лист папы:')
x = str(input())
y = str(input())
z = str(input())
w = str(input())
t = str(input())
print('Плей-лист мамы:')
print(f'{t}', f'{w}', f'{z}', f'{y}', f'{x}', sep='\n')

x = str(input('Номер рейса: '))
y = str(input('Название авиакомпании (на русском языке): '))
z = str(input('Название авиакомпании (на английском языке): '))
w = str(input('Город прилета (на русском языке): '))
t = str(input('Город прилета (на английском языке): '))
print(f'Заканчивается посадка на рейс {x} авиакомпании {y} до {w}')
print(f'This is the final boarding call for {x} flight {z} to {t}')

x = str(input('Как вас зовут? '))
print(f'Привет, {x}!')

x = 96
y = x//16
z = int(input())
c = (z - 48 * x)/y
print(c)

x = int(input())
y = int(input())
v = math.pi * (y ** 2)
b = math.pi * (x ** 2)
a = v - b
print(abs(a))

x = int(input())
z = (((((x+2) * 3) - 6) / 3) - 4)
print(z)

x = float(input())
y = x / 2.54
z = y / 12
w = z / 3
t = w / 1760
print(f'{w} ярдов', f'{t} мили', f'{z} футов', f'{y} дюймов', sep='\n')

