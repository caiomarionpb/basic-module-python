# 1. (n + n)
# 2. **
# 3. */ // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)
# aqui o python leu 1 + 1 + 5 = 7

# correto seria:
# o python le primeiro o que está entre parênteses
# depois a exponenciação, depois multiplicação/divisão/módulo e por último adição/subtração

conta_2 = (1 + 1) ** (5+5) # 1024
print(conta_2)
