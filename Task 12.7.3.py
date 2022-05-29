S = float(input("введите сумму вклада: "))
t = int(1)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
b1 = per_cent['ТКБ']
b2 = per_cent['СКБ']
b3 = per_cent['ВТБ']
b4 = per_cent['СБЕР']
bank1 = round(b1/100*S*t)
bank2 = round(b2/100*S*t)
bank3 = round(b3/100*S*t)
bank4 = round(b4/100*S*t)
print('Доход в ТКБ составит:',bank1,'Доход в СКБ составит:',bank2, 'Доход в ВТБ составит:',bank3,'Доход в СБЕР составит:',bank4)
maxi = round(max(per_cent.values()) / 100 * t)
bank = max(per_cent, key=per_cent.get)
print('\nВ банке', bank, 'будет максимальный доход')
