Grade = None
score = int(input("Enter score : "))

if(80 <= score <= 100):
    Grade = "A"
elif(70 <= score <= 79):
    Grade = "B"
elif(0 <= score <= 69):
    Grade = "F"
else:
    Grade = "N (invalid)"
    
print("Grade : ",Grade)