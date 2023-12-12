coffee = 1  # запас молотого кофе в кофейне (в килограммах)
milk = 2  # запас молока в кофейне (в литрах)

coffee_gram = coffee * 1000  # переводим килограммы кофе в граммы
milk_ml = milk * 1000  # переводим литры молока в миллилитры

espresso_coffee = 7  # количество кофе для эспрессо (в граммах)
latte_milk = 180  # количество молока для латте (в миллилитрах)
cappuccino_milk = 100  # количество молока для капучино (в миллилитрах)
visitors = 0  # количество посетителей, которых может обслужить кофейня

while coffee_gram >= espresso_coffee and milk_ml >= cappuccino_milk:
    visitors += 1
    coffee_gram -= espresso_coffee
    if visitors % 3 == 0 and visitors % 5 != 0:
        milk_ml -= cappuccino_milk
    if visitors % 5 == 0 and visitors % 3 != 0:
        milk_ml -= latte_milk
    if visitors % 3 == 0 and visitors % 5 == 0:
        milk_ml -= cappuccino_milk
print(visitors)
