"""

Formatação básica de strings
s - string
d - int
f - float
x ou X - hexadecimal (ABCDEF0123456789)
(Caractere) (><^) (quantidade) 
> - Esquerda
< - Direita
^ - Centro
= - força o numero aparecer antes dos zeros
sinal - + ou -
Ex.: 0>- 100, .1f
convertion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.86782545:0>+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')