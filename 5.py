num = int(input("Enter your number:"))
i = 1
while (True):
    if (num % i == 0):
        num /= i
else:
    break
i += 1
if (num == 1):
    print("Yes")
    else:
        print("No")
