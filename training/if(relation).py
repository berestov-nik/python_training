a = int(input())
b = a // 1000 % 10 + a % 10
c = a // 100 % 10 - a // 10 % 10
if b == c:
    print("ДА")
else:
    print("НЕТ")