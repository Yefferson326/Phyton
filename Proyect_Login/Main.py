from cleaner import cleaning

def message_welcome():
    print(" ___       _________  __________  ____  ___     ___")
    print("|   |     |         ||          ||    ||   \   |   |")
    print("|   |     |   ___   ||    ______||____||    \  |   |")
    print("|   |     |  |   |  ||   |______  ____ |     \ |   |")
    print("|   |     |  |   |  ||    ___   ||    ||      \|   |")
    print("|   |____ |  |___|  ||   |   |  ||    ||   |\      |")
    print("|        ||         ||   |___|  ||    ||   | \     |")
    print("|________||_________||__________||____||___|  \____|")


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
        print("¡¡USUARIO INCORRECTO!!\nPor favor ingreselo de nuevo")
        return valid_email


def valid_password(password):
    valid_password = False
    valid_long = 0
    while valid_password == False:
        for n in password:
            valid_long += 1
        if valid_long >= 8:
            print("Contraseña Valida")
            valid_password = True
        else:
            print("Tenga en cuenta que la constraseña debe ser de minimo 8 caracteres\nINGRESELA DE NUEVO")

        if valid_password:
            return valid_password
        else:
            print("¡¡USUARIO INCORRECTO!!\nPor favor ingreselo de nuevo")


def data_emails():
    registered_email = ["yefferson.nunez@uptc.edu.co", "Juan123@hotmail.com", "pepito753@gmail.com"]
    return registered_email


def data_passwords():
    passwords = ["123456", "Larompecorazones", "Solochico"]
    return passwords


def valid_data_base(email_user,password_user):
    passwords = data_passwords()
    emails = data_emails()
    check_email = False
    check_password = False

    for n in emails:
        for i in emails[n]:
            for d in Email:
                if email_user[d] == emails[n]:
                    check_email = True
                    for n in passwords:
                        for b in passwords[n]:
                            for c in password_user:
                                if password_user[c] == passwords[b]:
                                    check_password = True
                                    print("!!Ingreso completado con exito!!")
                                else:
                                    print ("!!El usuario o la contraseña no se encuentran en la base de datos por favor introduzcalos de nuevo!!")


message_welcome()
validate_ = False
while validate == False:
    Email = str(input("Digite la direccion de correo electronico\n-> "))
    validate = validate_email(Email)

password = str(input("Digite la constraseña:\n->"))
valid_password(password)
