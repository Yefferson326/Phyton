import Messages


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
    passwords = ['12345678', 'Juan123#', 'Contraseña']
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
        Messages.message_no_access()
    #Verifica si existe un email para poder mirar la respectiva contraseña de dicho email registrado
    if check_email == True:
        if passwords[position] == password_user:
            print("\t\t\t\U00002705Constraseña correcta\U00002705")
            Messages.message_access()
        else:
            print("\t\t\t\U000026A0Constraseña incorrecta\U000026A0")
            Messages.message_no_access()
