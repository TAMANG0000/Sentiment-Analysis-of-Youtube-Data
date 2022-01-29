import mysql.connector as connector
import smtplib
import random

connect = connector.connect(host="localhost", passwd="root", user="root", database="sentiment_analysis_youtube")
cursor = connect.cursor()


def login():
    count = 0
    email = input("Enter your email to login")
    selecting = "select * from reg_users;"
    cursor.execute(selecting)
    print(selecting + "Executing...")
    for i in cursor:
        if i[2] == email:
            print("Login Successful !")
            count = 1
            break
    if count == 0:
        print("Login Error !")

print("################### WELCOME ###################")
print("\n PLEASE ENTER 1 TO LOGIN, OR ENTER 2 TO REGISTER")

inp1=int(input())
count= 0

if inp1==1:
    login()
elif inp1==2:
    name = input("ENTER YOUR NAME: ")
    email = input("ENTER YOUR EMAIL: ")
    otp = str(random.randint(100000, 1000000))

    SUBJECT = "Here is your OTP for the Login Process"
    TEXT = "HEY " + name + '!' "\r\n""\r\n" 'Your OTP for login is: ' + otp + "\r\n""\r\n"\
    'Please enter the otp for further verification'"\r\n""\r\n"'Thank you !'
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('6149@apsjorhat.org', '12345678')
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail('group1@apsjorhat.org', email, message)
    s.quit()
    print("An OTP was sent to the entered email address")

    answer = int(input("Please enter the otp for verification"))
    if answer == int(otp):
        query = "insert into reg_users (Name,Email_ID) values (" + "'" + name + "'" + "," + "'" + email + "'" + ");"
        cursor.execute(query)
        connect.commit()
        print("You have been successfully registered. Now please follow the instructions to successfully Login ")
        login()

    else:
        print("Sorry,the otp you entered is incorrect")
elif inp1 != 1 and inp1 != 2:
    print("#### WRONG VALUES! PLEASE ENTER EITHER 1 OR 2 ####")