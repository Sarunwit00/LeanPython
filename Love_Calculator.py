def calculate_love_score(name1, name2):
    love = ["l" , "o" , "v","e"]
    true = ["t" , "r" , "u" , "e"]
    x = name1.lower()+name2.lower()
    love_sum = 0
    true_sum = 0
    for i in range(len(x)):
        if x[i] in love:
            love_sum += 1
        if x[i] in true:
            true_sum += 1
    print(str(true_sum)+str(love_sum))
    
    
calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Angela Yu", "Jack Bauer")
    
    
    
    