https://lab.karpov.courses/learning/243/module/2453/lesson/23855/68546/331882/


n_str = str(n)  # преобразуем число в строку
result = False  # начальное значение всегда False

for i in range(1, len(n_str)):
    digit = int(n_str[i])  # текущая цифра
    prev_digit = int(n_str[i - 1])  # цифра, стоящая слева от текущей
    is_multiple = (digit % prev_digit == 0)  # проверяем, кратна ли текущая цифра предыдущей
    result.append(is_multiple)  # добавляем результат проверки в массив

print(result)  # выводим результат


Тест, на котором получена ошибка

n = 736451
