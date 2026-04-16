print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on  your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0
#size S
if size == "S":
    total = total + 15
    if pepperoni == "Y":
        total = total + 2
    else:
        total = total + 0
        

# size M
elif size == "M":
    total = total + 20
    if pepperoni == "Y":
        total = total + 3
    else:
        total = total + 0
        

# size L
elif size == "L":
    total = total + 25
    if pepperoni == "Y":
        total = total + 3
    else:
        total = total + 0       
        
#extra cheese
if extra_cheese == "Y":
    total += 1
else:
    total += 0 

print(f"Your final bill is: ${total}.")