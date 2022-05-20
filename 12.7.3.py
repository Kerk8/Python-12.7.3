per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = int(input('Введите сумму вклада:'))
deposit = []
for key in per_cent:
    deposit.append(money*per_cent.get(key)/100)
print("Все проценты годовых по вкладам:", deposit)
print("Максимальная сумма процентов:", max(deposit))
