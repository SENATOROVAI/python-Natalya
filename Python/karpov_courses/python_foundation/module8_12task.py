https://lab.karpov.courses/learning/243/module/2453/lesson/23855/68546/331882/


n_str = str(n)  # преобразуем число в строку
result = False  # начальное значение всегда False
# сделай переменную result списком , с единственным значением False

for i in range(1, len(n_str)):
    digit = int(n_str[i])  # текущая цифра
    prev_digit = int(n_str[i - 1])  # цифра, стоящая слева от текущей
    is_multiple = (digit % prev_digit == 0)  # сделай двойную проверку , с использованием оператора and 
    # первая проверка должна быть на то не равняется ли prev_digit 0 ,иначе если ты этого не сделаешь 
    # то получишь ошибку errordivision by zero 
    result.append(is_multiple)  # сейчас ты пытаешься делать аппенд в переменную булевого типа,когда
    #ты сделаешь result списком то все будет работать нормально


print(result)  # выводим результат 



Тест, на котором получена ошибка

n = 736451
