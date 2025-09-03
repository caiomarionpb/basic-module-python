"""

flag (bandeira) - marcar um local
None = não valor
si e is not = é ou não é(tipo, valor, indentidade)
id = indentidade
"""

condicao = True
passou_no_if = None

if condicao:
   passou_no_if = True
   print('faça algo')
else:
  print('não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
   print('Não passou no if')

if passou_no_if is not None:
   ('passou no if')