n = int(input())

liters_poured= 0

for i in range(n):
    l = int(input())
    liters_poured += l
    if liters_poured > 255:
        print("Insufficient capacity!")
        liters_poured -= l
print(liters_poured)