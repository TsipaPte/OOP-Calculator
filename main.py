""" Импортируем модуль decimal для точечных операций с дробными числами """

import decimal

class Calculator:
    """ Главный класс для вычислений (калькулятор) """
    def __init__(self, expression: str) -> None:
        """ Инициализатор атрибутов """
        self.exp = expression

    def calculate(self):
        """ Основная функция для вычисления выражения """
        calc = self.exp.split()

        try:
            a = decimal.Decimal(calc[0])
            b = decimal.Decimal(calc[2])
        except decimal.InvalidOperation:
            return "[errno] Ошибка в значениях"
        except IndexError:
            return "[errno] Ошибка длины"
        except Exception as e:
            return f"[errno] Неизвестная ошибка. Если вы её видите, то сообщите разработчику. Ошибка: {e}"

        if len(calc) == 3:
            match calc[1]:
                case "+":
                    return a + b
                case "-":
                    return a - b
                case "*":
                    return a * b
                case "/":
                    try:
                        return a / b
                    except ZeroDivisionError:
                        return "[errno] Делить на ноль нельзя"
                case _:
                    return "[errno] Неизвестный оператор"
        else:
            return "[errno] Выражение должно быть в следующем формате: X Y Z где x и z - переменные, а y - оператор"

    def __str__(self):
        """ Функция для отображения красивого вывода """
        return f"{self.calculate()}"

def main():
    """ Главная функция main """
    user_expression = Calculator(input("Введите значение в следующем формате: x oper y: "))

    print(user_expression)

if __name__ == "__main__":
    main()
