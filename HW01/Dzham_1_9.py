abn = input()
abn = map(int, abn.split())
a, b, n = abn
cost = a*100 + b
fee = (cost * n)
fee1 = fee //100
fee2 = fee %100
print(fee1, fee2)