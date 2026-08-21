def limpar(texto):
    return texto.strip().replace('.', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')

cpf = " 123.456.789-00 "
telefone = "(11) 99999-8888"

print("CPF limpo:", limpar(cpf))
print("Telefone limpo:", limpar(telefone))
