n = input()
sum_a = sum(map(int, n[:3]))
sum_b = sum(map(int, n[-3:]))
print(['Обычный', 'Счастливый'][sum_a==sum_b])