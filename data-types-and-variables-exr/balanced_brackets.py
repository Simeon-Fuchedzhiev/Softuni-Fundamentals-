n = int(input())
sum = 0
for i in range(n):
    sym = input()
    
        try:
            x = ord('sym')
        except (ValueError, TypeError):
            continue
    
    
    if ord('sym') == 40 or ord('sym') == 41:
        sum += ord(sym)
    else:
        continue
    if sum == 81:
        sum = 0
if sum == 0:
    print("BALANCED")
else:
    print("UNBALANCED")