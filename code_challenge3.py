name = input("What is your name? --> ")
fare = eval(input("How much is your fare fee? --> "))
student = input("Are you a student? --> ")

if student == "yes":
           discount = fare * 0.2
           discounted_fare = fare - discount
           print(name, "You'll have a discount of 20%")
           print("Therefore, your new fare is", discounted_fare)
else:
           print("Since you're not a student, you're fee will not be discounted bt 20%")