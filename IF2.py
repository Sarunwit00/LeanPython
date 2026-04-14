
username = input("Entername : ")
password = input("Enterpassword : ")

if username == "member" and password == "1234" :
        number = int(input("Enter_Number : "))
        if number == 1 :
            print("ถอนเงิน")
        elif number == 2:
            print("ฝากเงิน")
        else:
            print("หมายเลขบริการไม่ถูกต้อง")
else:
    print("Not find Account")