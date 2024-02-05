import random

def escolha_jogador():
    escolha = input('Escolha: Pedra, Papel e tesoura.').lower()
    while escolha not in ['pedra', 'papel','tesoura']:
        print('Escolha inválida. Tente novamente.')
        escolha = input('Escolha pedra, papel ou tesoura: ').lower()
    return escolha

def maquina():
    return random.choice(['pedra','papel', 'tesoura'])

def desenho(escolha):
    arte_pedra = """
         ---  ---  ---
 ----/   \/   \/   \ 
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
\___/\___/ ----------- 
|         |            |  
|          -----------/ 
|                    /
\                   /
 \                 /        
  ----------------- 
"""

    arte_papel = """
 ___  ___  ___  ____
/   \/   \/   \/    \\
|    |    |    |    |
|    |    |    |    | ___
|    |    |    |    |/   \\   
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|                        |
|                       /
|                      /
\                     /
 \                   /        
  -------------------
"""

    arte_tesoura = """
 ___  ___  ___  ____
/   \/   \/   \/    \\
|    |    |    |    |
|    |    |    |    | ___
|    |    |    |    |/   \\   
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
\___/\____/ -----------\\
|         |            |  
|          -----------/ 
|                    /
\                   /
 \                 /        
  ------------------- 
"""

    return {
    "pedra": arte_pedra,
    "papel": arte_papel,
    "tesoura": arte_tesoura
}.get(escolha, "Arte não encontrada.")

def vencedor(escolha_usuario, escolha_computador):
    arte_jogador = desenho(escolha_usuario)
    arte_computador = desenho(escolha_computador)

    print(f"\nUsuário: {escolha_usuario}\n{arte_jogador}")
    print(f"Computador: {escolha_computador}\n{arte_computador}")
    print(f"Resultado: {escolha_usuario} x {escolha_computador}")

    if (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
       (escolha_jogador == "papel" and escolha_computador == "pedra") or \
       (escolha_jogador== "tesoura" and escolha_computador == "papel"):
        return "Você venceu!  (─‿‿─)"
    
    
    elif escolha_jogador == escolha_computador:
        return 'Empate!  (◑‿◐)'
    else:
        return 'Você perdeu! (｡•́︿•̀｡)'

def main():
    print('Bem-vindo ao Jogo Jokenpo!')

    while True:
        escolha_usuario = escolha_jogador()
        escolha_computador = maquina()

        resultado = vencedor(escolha_usuario, escolha_computador)
        print(resultado)

        jogar_novamente = input('\nQuer jogar novamente? (s/n):').lower()
        if jogar_novamente != 'Sim':
            break

if __name__ == '__main__':
    main()