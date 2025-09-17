print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER!")
phrase = input("Enter a phrase for the parrot to repeat: ")
times = int(input("How many times should the parrot repeat it? "))

print("🦜 Parrot says:")

i = 0
for i in range(times):
    print("🦜 Squawk!", phrase)
    
