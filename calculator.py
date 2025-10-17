def ADD(x,y):
    # 1. Нарушение PEP 8 - неправильные имена и пробелы
    return x+y

def subtract(a, b):
    # 2. Избыточный код
    result = a - b
    return result

def multiply(a, b):
    # 3. Неочевидное именование переменных
    r = a * b
    return r

def divide(a, b):
    # 4. Потенциальное деление на ноль
    return a / b

def main():
    # 5. Магические числа
    print("Калькулятор")
    
    # 6. Отсутствие обработки ошибок ввода
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    
    # 7. Нестандартное меню
    print("1-сложить 2-вычесть 3-умножить 4-делить")
    choice = input("Выбери: ")
    
    if choice == "1":
        result = ADD(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        print("Неверно")
        return
    
    # 8. Проверка на магическое число
    if result > 100:
        print("Большой результат!")
    
    print(f"Ответ: {result}")

if __name__ == "__main__":
    main() 
