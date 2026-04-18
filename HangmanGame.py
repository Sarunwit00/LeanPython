import random

def create_Word(List):
    word = ""
    for i in range(len(List)):
        word = word+List[i]
    return word
    
word_list = ["apple", "baboon","camel"]
chosen_word = random.choice(word_list)
x , y = [] , []
for i in range(len(chosen_word)):
    y.append(chosen_word[i])
    x.append("_")    
# print(x)
# print(y)

while True:
    letter = input("Guess a Letter : ").lower()
    if letter == "/":
        break
    elif letter in y :
        for i in range(len(y)):
            if letter == y[i]:
                x[i] = letter
        print("True",end="  ")    
        print(x)
        if create_Word(x) == create_Word(y):
            print("You Win")
            break
    else:
        print("False",end="  ")
        print(x)
        

