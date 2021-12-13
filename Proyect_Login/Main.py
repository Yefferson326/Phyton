from Messages import message_welcome
import validate_method


message_welcome()
password_correct = False
email_correct = False
while email_correct == False:
    email_user = str(input("Digite la direccion de correo electronico\n-> "))
    email_correct = validate_method.validate_email(email_user)
while password_correct == False:
    password = str(input("Digite la constraseña:\n->"))
    password_correct = validate_method.valid_password(password)

validate_method.valid_data_base(email_user,password)