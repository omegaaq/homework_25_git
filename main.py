print('hello')

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