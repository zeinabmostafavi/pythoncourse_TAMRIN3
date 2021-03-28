array = []
a = int(input("enter tool:"))
for i in range(0, a):
    x = int(input("enter number"))
    array.append(x)
    print(array)
    if array == sorted(array):
        print('sorted')
    else:
        print('not sorted')
