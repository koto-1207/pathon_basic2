import random

dice_faces = int(input("サイコロの面の数は?: "))
roll_times = int(input("何回振りますか?: "))
results = []

for i in range(roll_times):
    dice_roll = random.randint(1, dice_faces)
    results.append(dice_roll)


print(results)
