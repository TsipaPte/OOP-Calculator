import decimal

class Calculator:
    def __init__(self, expression: str) -> None:
        self.exp = expression

    def calculate(self):
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
        return f"{self.calculate()}"

userExpression = Calculator(input("Введите значение в следующем формате: x oper y: "))

print(userExpression)
