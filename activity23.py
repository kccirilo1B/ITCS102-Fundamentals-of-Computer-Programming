username = input("Enter your username: ")
fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango']

fruits.append("Kiwi")
print(f"\n---FRUIT LIST COMPILATION, {username}---")
print(f"\nHello {username}, here is the updated list of Fruits: {fruits}\n")
fruits.insert(2, "Strawberry")
print(f"After inserting a new fruit at index 2, the list is now: {fruits}\n")
fruits.remove("Grapes")
print(f"After removing 'Grapes', the list is now: {fruits}\n")
fruits.sort()
print(f"After sorting the list alphabetically, it is now: {fruits}\n")
fruits.reverse()
print(f"After reversing the list, it is now: {fruits}\n")
fruits.pop()
print(f"After popping the last fruit from the list, it is now: {fruits}\n")
print(f"Total number of fruits in the list: {len(fruits)}\n")
print("------------------------------------------------------------------------------------------------------------------------------------------\n")

print("Thank You for Trying the Fruit List Compilation!")
 
