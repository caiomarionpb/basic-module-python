"""

CONSTANTE = "Variáveis" que não vão mudar
muitas condições no mesmo if(ruim)
    <- contagem de complexidade(ruim)

"""

velocidade = 100 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

# CONSTANTES    
RADAR_1 = 60 # velocidade máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar está

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar_1 and vel_carro_passou_radar_1


if vel_carro_passou_radar_1:
    print('Velocidade carro passou radar 1')

if carro_passou_radar_1:
    print('carro passou radar 1')

if carro_multado_radar1:
    print('carro foi multado em radar 1')

