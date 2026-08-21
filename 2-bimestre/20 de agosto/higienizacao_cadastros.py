def higienizar_nome(nome):
    return nome.strip().upper()


def higienizar_email(email):
    return email.strip().lower()


if __name__ == "__main__":
    nome_entrada = " joão pedro da silva "
    email_entrada = " JOAO.SILVA@Escola.COM "

    nome_higienizado = higienizar_nome(nome_entrada)
    email_higienizado = higienizar_email(email_entrada)

    print("Nome higienizado:", nome_higienizado)
    print("E-mail higienizado:", email_higienizado)
