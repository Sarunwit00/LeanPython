username = input("ป้อนชื่อผู้ใช้ : ")
password = input("ป้อนpassword : ")

if(not username == "admin" and password == "1234"):
    print("connect pass")
else:
    print("Error Connect")