dan = int(input("行数を入力してください:"))
retu = int(input("列数を入力してください:"))

for dan in range(1, dan + 1):
    for i in range(1, retu + 1):
        calc = dan * i
        print(calc, end=" ")
    print()
