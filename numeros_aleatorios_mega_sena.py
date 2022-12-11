from random import randint
from time import sleep
quant = int(input('Quantos jogos você quer fazer? '))
tot =1
jogos = []
sorteado = []
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,61)
        if num not in sorteado:
            sorteado.append(num)
            cont +=1
        if cont >=6:
            break
    sorteado.sort()
    jogos.append(sorteado[:])
    sorteado.clear()
    tot +=1
print('*' * 5, f'Sorteando {quant} Jogos', '*' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('Boa Sorte...')