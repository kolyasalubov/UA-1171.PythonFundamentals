#2nd version of password validation

from passvalidator import passwordValidator

""" 1st importing our module 'passValidator' 
    2nd write that the loop 'while' will be runnig before coinditio will not be executed 
    3rd if validation True , the cicle break and outputing message 'Welcome' 
    else message 'Wrong password.Try more' """
    
while True:
    password = input("Write your password: ")

    if passwordValidator(password):
        print ("Welcome")
        break
    else:
        print ("Wrong password.Try more")
        
