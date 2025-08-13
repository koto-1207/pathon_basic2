# 式が表示されている
# 結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい
# ※結果が3桁の場合は崩れてもOKで

dan = 9
retu = 9

for dan in range(1, dan + 1):
    for i in range(1, retu + 1):
        product = dan * i
        calc = f"{dan} X {i} = {product} |"
        
        print(calc, end=" ")
    print()
