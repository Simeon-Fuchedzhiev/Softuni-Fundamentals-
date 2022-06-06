from math import floor
group_size = int(input())
days = int(input())

coins = 0

total_money = days * 50
food_def = group_size * 2

motivarional_party_money_def = (days // 3) * (group_size * 3)
boss_money_inc = (days // 5) * (group_size * 20)
for i in range(1, days +1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    coins +=  50 - (group_size * 2)
    if i % 3 == 0:
        coins -= group_size * 3
    if i % 5 == 0:
        coins += 20 * group_size
    if i % 5 == 0 and i % 3 == 0:
        coins -= 2 * group_size
coins_per_companion = floor(coins / group_size)

print(f"{group_size} companions received {coins_per_companion} coins each.")