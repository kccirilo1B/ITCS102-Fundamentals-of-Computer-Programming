name = input("Enter your name: ")
print("SUMMATION OF ODD NUMBER, enter 0 to stop")
kc = True
sum = 0
odd = ""

while kc == True:
      num = eval(input("Enter a random number: ")) 
     
      if num % 2 == 1:
            print("ODD NUMBER, continue ")
            sum += num
            odd += str(num) + " "
            continue
      elif num == 0:
            print("okay, stop na") 
            break
      else:
            if num % 2 == 0:
                 print("EVEN NUMBER, continue ")
            else:
                 print("INVALID OY")
            continue
print(f"Hello {name}, the sum of all ODD number is {sum} ")
print(f"ODD numbers detected are {odd}") 
