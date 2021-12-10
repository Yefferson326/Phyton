
def message_welcome():
    print("\t\t ___       _________  __________  ____  ___     ___")
    print("\t\t|   |     |         ||          ||    ||   \   |   |")
    print("\t\t|   |     |   ___   ||    ______||____||    \  |   |")
    print("\t\t|   |     |  |   |  ||   |______  ____ |     \ |   |")
    print("\t\t|   |     |  |   |  ||    ___   ||    ||      \|   |")
    print("\t\t|   |____ |  |___|  ||   |   |  ||    ||   |\      |")
    print("\t\t|        ||         ||   |___|  ||    ||   | \     |")
    print("\t\t|________||_________||__________||____||___|  \____|")


def message_no_access():
    print("\n\t\t\t\t\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C")
    print("\t\t\t\t  REGISTRO INCORRECTO")
    print("\t\t\t\t\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C\U0000274C")


def message_access():
    print("\n\t\t\t\t\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611")
    print("\t\t\t\t REGISTRO CORRECTO")
    print("\t\t\t\t\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611\U00002611")


def validate_email(email):
    valid_email = False
    valid_at_sing = 0
    valid_point = 0
    for n in email:
        if n == '@':
            valid_at_sing += 1
            valid_email = True
        elif n == '.':
            valid_point += 1
        elif valid_at_sing != 1 and valid_point < 1:
            valid_email = False

    if valid_email:
        return valid_email
    else:
        print("\t   ¡¡USUARIO INCORRECTO!!\n\t\U000026A0Por favor ingreselo de nuevo\U000026A0")
        return valid_email


def valid_password(password):
    check_password = False
    valid_long = 0
    while check_password == False:
        for n in password:
            valid_long += 1
        if valid_long >= 8:
            check_password = True
        else:
            print("\t\U000026A0Tenga en cuenta que la constraseña debe ser de minimo 8 caracteres\U000026A0")

        if check_password:
            return check_password
        else:
            print("\t\t\t\t¡¡INGRESA DE NUEVO LA CONSTRASEÑA¡¡")
            return check_password


def valid_data_base(email_user, password_user):
    registered_email = ['yefferson.nunez@uptc.edu.co', 'Juan123@hotmail.com', 'pepito753@gmail.com']
    passwords = ['12345678', 'Larompecorazones', 'Solochico']
    check_email = False
    check_password = False

    for email_select in registered_email:
        if email_user == email_select:
            check_email = True
            print("\t\t\U00002705El correo se encuentra en la base de datos\U00002705")
            position = registered_email.index(email_select)
            break

    if check_email != True:
        print("\t\t\U000026A0El correo no se encuentra en la base de datos\U000026A0\n\t\t\t    ¡¡POR FAVOR VERIFIQUE EL CORREO¡¡")
        message_no_access()
    #Verifica si existe un email para poder mirar la respectiva contraseña de dicho email registrado
    if check_email == True:
        if passwords[position] == password_user:
            print("\t\t\t\U00002705Constraseña correcta\U00002705")
            message_access()
        else:
            print("\t\t\t\U000026A0Constraseña incorrecta\U000026A0")
            message_no_access()


message_welcome()
password_correct = False
email_correct = False
while email_correct == False:
    Email = str(input("Digite la direccion de correo electronico\n-> "))
    email_correct = validate_email(Email)
while password_correct == False:
    password = str(input("Digite la constraseña:\n->"))
    password_correct = valid_password(password)

valid_data_base(Email,password)