per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} #Банковский словарь

money = int(input("Введите планируемую сумму вклада: "))

deposit_values = list(per_cent.values()) #Создаем список из значений словаря

#Находим значение накопленных средств за год
for dep in range (len(deposit_values)):
    deposit_values[dep] *= money/100

deposit_int = list(map(int, deposit_values)) #Список накопленных средств в целочисленном формате

deposit = "deposit = " + str(deposit_int)

max_val = "Максимальная сумма, которую вы можете заработать - " + str(max(deposit_int))

print(deposit)

print()

print(max_val)