n = int(input("Enter the amount to deposit: "))
print("Here is the breakdown of the deposited amount:")

d1 = n // 1000
n = n - (d1 * 1000)

d2 = n // 500
n = n - (d2 * 500)

d3 = n // 200
n = n - (d3 * 200)

d4 = n // 100
n = n - (d4 * 100)

d5 = n // 50
n = n - (d5 * 50)

d6 = n // 20
n = n - (d6 * 20)

d7 = n // 10
n = n - (d7 * 10)

d8 = n // 5
n = n - (d8 * 5)

d9 = n // 1
n = n - (d9 * 1)

print("1000 : ", d1)
print("500 : ", d2)
print("200 : ", d3)
print("100 : ", d4)
print("50 : ", d5)
print("20 : ", d6)
print("10 : ", d7)
print("5 : ", d8)
print("1 : ", d9)
