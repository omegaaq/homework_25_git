print('hello')

def read_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            res = file.read()
            print(int(res))
    except FileNotFoundError:
        print('file not founded')


file_name = 'number.txt'
read_from_file(file_name)

i = 0
while i != 4:
    print('1 - задати число\n2 - змінити\n3 - занулити\n4 - вийти з меню')
    user_input = int(input('enter number of your chice: '))
    if user_input == 4:
        print('bye')
        break
    else:
        if user_input == 1:
            print('1')
        elif user_input == 2:
            print('2')
        elif user_input == 3:
            print('3')