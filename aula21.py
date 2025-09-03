# operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições devem ser verdadeiras
# se qualquer valor for considerado falso, a expressão inteira será falsa
# 0 0.0 '' False
# também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
   print('entrar')
else:
   print('sair')


# avaliação de curto-circuito
print(True and 0 and True)  # False
print(bool('')) # False
