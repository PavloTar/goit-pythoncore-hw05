# ЗАВДАННЯ 4

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.
# (ДЗ завдання 4) Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати
# відповідно до введеної команди.
# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.


# Ініціалізація словника для збереження контактів (ім'я -> телефон)
contacts = {}

# Декоратор для обробки помилок введення користувача
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command. Usage: command [name] [phone]"

    return inner


# Функція для розбору введеного користувачем рядка
def parse_input(user_input):
    command_parts = user_input.lower().split()
    if not command_parts:
        return ("Invalid command",)
    
    command = command_parts[0]
    args = command_parts[1:]
    
    return (command, args)

# Функція для додавання контакту з декоратором обробки помилок
@input_error
def add_contact(args, contacts):
    name, phone = args
    if not name or not phone:
        raise ValueError
    contacts[name] = phone
    return "Contact added."

# Функція для зміни номера телефону контакту з декоратором обробки помилок
@input_error
def change_contact(args, contacts):
    name, phone = args
    if not name or not phone:
        raise ValueError
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

# Функція для виведення номера телефону контакту з декоратором обробки помилок
@input_error
def show_phone(args, contacts):
    name = args[0]
    if not name:
        raise ValueError
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

# Функція для виведення всіх контактів без декоратора (оскільки вона не повертає значення)
def show_all():
    if contacts:
        print("\n".join(f"{name}: {phone}" for name, phone in contacts.items()))
    else:
        print("No contacts available.")

# Основна функція для управління взаємодією з користувачем
def main():
    print("Welcome to the assistant bot!")
    print("How can I help you? Type 'help' for command information.")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        # Логіка обробки різних команд
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all()
        elif command == "help":
            print("Available commands:")
            print("  - hello")
            print("  - add [name] [phone]")
            print("  - change [name] [phone]")
            print("  - phone [name]")
            print("  - all")
            print("  - close or exit")
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Type 'help' for command information.")

# Початок виконання програми, якщо цей файл запускається
if __name__ == "__main__":
    main()