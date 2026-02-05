import random

times = int(input("請輸入要擲骰子的次數："))

results = []

for i in range(times):
    dice = random.randint(1, 6)
    results.append(dice)

print("擲骰子的結果是：", results)
