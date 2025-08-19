dan = 9
retu = 9

for dan in range(1, dan + 1):
    for i in range(1, retu + 1):
        product = dan * i
        calc = f"{dan} X {i} = {product:2}"

        print(calc, end=" | ")
    print()
