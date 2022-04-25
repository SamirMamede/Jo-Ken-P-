from random import randint
from time import sleep

print(10*'=-', 'JO - KEN - PÔ', 10*'=-')
print('Escolha entre:\n[ 0 ] - Pedra\n[ 1 ] - Papel\n[ 2 ] - Tesoura')
print('Para encerrar digite 3 !!')
itens = ['Pedra', 'Papel', 'Tesoura']
while(True):
    computador = randint(0, 2)
    jogador = int(input('Faça sua jogada: '))
    if jogador == 3:
        print('GAME OVER !!')
        break
    if jogador > 3:
        print('Entrada inválida !!')
        continue
    print('JO')
    sleep(1)
    print('ken')
    sleep(1)
    print('PÔ !!')
    print(f'Você escolheu {itens[jogador]}')
    print(f'Computador escolheu {itens[computador]}')
    if computador == 0:
        if jogador == 0:
            print('Empataram, tente novamente !!')
        elif jogador == 1:
            print('Você ganhou, parabéns !!')
        elif jogador == 2:
            print('Você perdeu !! Mais sorte na próxima.')   
    elif computador == 1:
        if jogador == 0:
            print('Você perdeu !! Mais sorte na próxima.')
        elif jogador == 1:
            print('Empataram, tente novamente.')
        elif jogador == 2:
            print('Você venceu !! Parabéns !!')
    elif computador == 2:
        if jogador == 0:
            print('Você venceu !! Parabéns !!')
        elif jogador == 1:
            print('Você perdeu !! Mais sorte na próxima.')
        elif jogador == 2:
            print('Empataram, tente novamente !!')  