dan = int(input("行数を入力してください: "))
retu = int(input("列数を入力してください: "))

for d in range(1, dan + 1):
    for i in range(1, retu + 1):
        product = i * d
        calc = f"{i} X {d} = {product:2}"
        print(calc, end=" | ")
    print()

