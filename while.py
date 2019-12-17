number = 1
while number <= 3500:
    #this is what we do to print even numbers ==
    #the exclamation is the not symbol for the odd numbers !=
    #if number % 2 == 0:
     print(number)
     number = number + 1

L = []
while len(L) <3:
    new_name = input("Please enter a new name:").strip().capitalize()
    L.append(new_name)

print("Sorry list is full!")
print(L)
    
