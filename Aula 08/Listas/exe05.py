n = 1
i = 0
i2 = 0
i3 = 0
i4 = 0

while n >= 0:
    n = int(input('digite um valor: '))
    if 0<n<25:
        i += 1
    elif 26<n<50:
        i2 += 1
    elif 51<n<75:
        i3 += 1
    elif 76<n<100:
        i4 += 1
    else:
        print


print(i)
print(i2)
print(i3)
print(i4)


