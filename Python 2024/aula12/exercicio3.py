''' o aventureiro encontrou outro assaltante pelo caminho, mas agora ele esta mais treinado, imediatamente foi para o combate
sabendo que cada personagem tem uma quantidade inicial de "vida" e um valor de "ataque" seguindo a seguinte estrututa:'''

import time, random

aventureiro =[ [ "vida", "ataque base"],
              [1000 , 30  ],
              ]

assaltante =[["vida", "ataque base"],
             [600, 20],
             ]



# o aventureiro e o assaltante atacam simultaneamente, causando dano um ou outro com o valor de "ataque".
# a batalha continua  ate a "vida " de um dos personagens chegue a zero ou a baixo"
#apos cada rodada de ataque os status de cada personagem (seus valores de "vida" e "ataque" )deve ser exibido
#havera um intervalo de 4 segundos entre as rodadas de ataque simular a pausa entre os golpes.
# ao final da batalha, o loop deve parar e os valores finais de "vida " de ambos os personagens devem ser mostrados.


while assaltante[1][0] > 0 and aventureiro[1][0] > 0:
    Variavelaventureiro = random.randint(1, 30)
    Variaveassaltante = random.randint(1, 20)
    assaltante[1][0] -= 20 * Variaveassaltante
    aventureiro[1][0] -= 20 * Variaveassaltante
    print("Status aventureiro:")
    for linha in aventureiro:
        print(linha)
    print(f"multiplicador de critico:", Variavelaventureiro)
    print("Status assaltante:")
    for linha in assaltante:
        print(linha)
    print(f"multiplicador de critico:", Variaveassaltante)
    time.sleep(4)




   
