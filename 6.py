num = input('Enter your number:')
y = 0
c = len(num)
for m in range(c):
    x = int(num[m])**c
    y += x
    if y == int(num):
        print("Yes")
    else:
        print("No")
