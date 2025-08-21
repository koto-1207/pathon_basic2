def total_num():
    total = 0
    for i in numbers:
        total += i
    return total


# 最大値
def max_num():
    max = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max


# 最小値
def min_num():
    min = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
    return min


# 平均値
def avg_num():
    return total_num() // len(numbers)


data = input("データを入力してください（スペース区切り）：")
numbers = []
for item in data.split():
    numbers.append(int(item))

print(f"合計値: {total_num()}")
print(f"最大値: {max_num()}")
print(f"最小値: {min_num()}")
print(f"平均値: {avg_num()}")
