def greeting(name):
    print('Hello', name, '\n', "Hope you are doing well", name, '\n', "Nice to meet you", name)


def greetings(first_name, last_name):
    print('Hello,', first_name, last_name)


def addition(first_number, second_number):
    print('The sum of', str(first_number), 'and', str(second_number), 'is', str(first_number + second_number))


def addition_return(first_number, second_number):
    return first_number + second_number


def main():
    name_list = []

    for i in range(3):
        name = input('Enter your name: ')
        name_list.append(name)

    for i in range(3):
        greeting(name_list[i])

    for i in range(3):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        greetings(first_name, last_name)
    for i in range(3):
        first_number = int(input('Enter a number: '))
        second_number = int(input('Enter a number: '))
        addition(first_number, second_number)

    first_number = int(input('Enter a number: '))
    second_number = int(input('Enter a number: '))
    print('The sum of', str(first_number), 'and', str(second_number), 'is',
          str(addition_return(first_number, second_number)))


if __name__ == "__main__":
    main()
