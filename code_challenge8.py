print("MULTIPLICATION TABLE MAKER")
num = eval(input("Enter a number: "))
print("Multiplication table for", num, ":")
i = 1
for i in range(1, 11):
     product = num * i
     print(num, "x", i, "=", product)
     i = i + 1
