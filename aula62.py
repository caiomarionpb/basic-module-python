"""
lista de listas e seus índices
"""

salas = [
    #   0         1
    ['maria', 'helena', ], #0
    # 0
    ['elaine', ], # 1            0  1  2  3  4
    #  0        1        2       3  
    ['luiz', 'joão', 'eduarda', (0,10,20,30,40)], # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'a sala é {sala}')
    for aluno in sala:
        print(aluno)
