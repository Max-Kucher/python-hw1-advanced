import string
import random


def generate_password(length):
    if length < 8:
        print("Длина пароля должна быть хотя бы 8 символов.")
        return None

    all_characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = [random.choice(string.ascii_uppercase),
                    random.choice(string.ascii_lowercase),
                    random.choice(string.digits),
                    random.choice(string.punctuation)]

        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        random.shuffle(password)
        generated_password = ''.join(password)

        if (any(c.islower() for c in generated_password) and
                any(c.isupper() for c in generated_password) and
                any(c.isdigit() for c in generated_password) and
                any(c in string.punctuation for c in generated_password)):
            return generated_password


def password_generator():
    print("\nДобро пожаловать в генератор паролей для пользователей Linux!\n")

    while True:
        length_input = input("Введите желаемую длину пароля: ")
        try:
            length = int(length_input)
        except ValueError:
            print("\nОшибка: введено некорректное значение. Необходимо ввести число.")
            continue

        print("\nСгенерированный пароль: ", generate_password(length))
        repeat = input("\nХотите сгенерировать еще пароль? (Y/N): ")
        if repeat.lower() != 'y':
            break


password_generator()
