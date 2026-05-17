

password = input("Enter your password: ")

def pass_validation(password):
        if not any(char.isupper() for char in password):
            print("Use atleast one uppercase")
        elif not any(char.islower() for char in password):
            print("Use atleast one lowercase")
        elif not any(char in '%$#@!&*' for char in password):
            print("Add atleast one special character")
        elif len(password) < 8:
            print("password need to be atleast 8 character")
        else: 
            print("Your password is :", password)
       
pass_validation(password)