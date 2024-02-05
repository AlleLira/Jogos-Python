import time
import random

def digitando_mensagem(mensagem):
    for char in mensagem:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print('\n')

def nome_jogador():
    print('Bem-vindo à busca pela Cenoura Sagrada, corajoso coelho!')
    digitando_mensagem('Me diga seu nome pequeno Coelho: ')
    nome = input()
    return nome

def mensagem_inicial(nome):
    mensagem = f"{nome}, você está pronto para começar a sua maior aventura?"
    digitando_mensagem(mensagem)

def escolher_rota_inicial():
    digitando_mensagem(['Escolha sua rota inicial:', '\n1. Caminho da Floresta Mística', '\n2. Túneis Subterrâneos Sombrios'])
    escolha = input('Digite o número da rota escolhida: ')
    return escolha

def rolar_dado():
    return random.randint(1,6)

def combate():
    vida_jogador = 3
    vida_monstro = 6

    while vida_jogador > 0 and vida_monstro > 0:
      input('\nPressione Enter para lançar o dado e atacar o monstro...')
      dano_jogador = rolar_dado()
      print(f"Você causou {dano_jogador} ponto de dano ao monstro.")

      vida_monstro -= dano_jogador

      if vida_monstro <= 0:
        print('Você derrotou o monstro! Continue sua jornada.')
        break

      input('\nPressione Enter para o monstro atacar...')
      dano_monstro = rolar_dado()
      print(f"O monstro causou {dano_monstro} pontos de dano em você.")
      vida_jogador -= dano_monstro

      if vida_jogador <= 0:
        print('Você foi derrotado pelo mosntro. Game Over!!!')

    return vida_jogador> 0
def primeira_trilha(rota_escolhida):
    if rota_escolhida == '1':
        digitando_mensagem('Você segue pelo Caminho da Floresta Mística.')
        time.sleep(2)
        digitando_mensagem(['\n1. Entrar no Bosque Encantado.', '\n2. Cruzar a ponte do Mistério.'])
        escolha = input('Qual caminho você deseja continuar: ')
        return escolha
    elif rota_escolhida == '2':
        digitando_mensagem('Você adentra os Túneis Subterrâneos Sombrios.')
        time.sleep(2)
        digitando_mensagem(['\n3. Explorar a Caverna Escura.', '\n4. Seguir a Trilha dos Luminescentes.'])
        escolha = input('Qual caminho você deseja continuar: ')
        return escolha

def segunda_trilha(escolha_segunda_trilha):
    if random.choice([True, False]):
        digitando_mensagem('Oh não, um monstro apareceu em seu caminho! \n Derrote ele para poder continua!')
        vitoria = combate()
        if vitoria:
          if escolha_segunda_trilha == '1':
              digitando_mensagem('Você escolhe explorar o Bosque Encantado.')
              time.sleep(2)
              digitando_mensagem(['\n1. Siga a trilha de florestas mágicas.', '\n2. Suba na árvore gigante.', '\n3. Desvie do riacho encantado.'])
              escolha = input('Qual caminho você deseja continuar: ')
              return escolha
          elif escolha_segunda_trilha == '2':
                digitando_mensagem('Você decide cruzar a Ponte do Mistério.')
                time.sleep(2)
                digitando_mensagem(['\n4. Desça para a Caverna Subaquática.', '\n5. Atravesse a Planície dos Fantasmas.', '\n6. Escale a Montanha Nebulosa'])
                escolha = input('Qual caminho você deseja continuar: ')
                return escolha
          elif escolha_segunda_trilha == '3':
                digitando_mensagem('Você opta por explorar a Caverna Escura.')
                time.sleep(2)
                digitando_mensagem(['\n7. Desbrave as Profundezas Sombrias.', '\n8. Enfrente os Morcegos da Escuridão.', '\n9. Siga a luz fraca à distância.'])
                escolha = input('Qual caminho você deseja continuar: ')
                return escolha
          elif escolha_segunda_trilha == '4':
                digitando_mensagem('Você segue a Trilha dos Luminescentes.')
                time.sleep(2)
                digitando_mensagem(['\n10. Investigue as flores brilhantes.', '\n11. Passe pelos Túneis de Cristal.', '\n12. Fuja dos Esporos Venenosos.'])
                escolha = input('Qual caminho você deseja continuar: ')
                return escolha

        else:
            digitando_mensagem('Ho não, sinto muito por você, estarei rezando ao Deus das cenouras por sua pobre alma.')
            return'13'
    else:
      if escolha_segunda_trilha == '1':
        digitando_mensagem('Você escolhe explorar o Bosque Encantado.')
        time.sleep(2)
        digitando_mensagem(['\n1. Siga a trilha de florestas mágicas.', '\n2. Suba na árvore gigante.', '\n3. Desvie do riacho encantado.'])
        escolha = input('Qual caminho você deseja continuar: ')
        return escolha
      elif escolha_segunda_trilha == '2':
        digitando_mensagem('Você decide cruzar a Ponte do Mistério.')
        time.sleep(2)
        digitando_mensagem(['\n4. Desça para a Caverna Subaquática.', '\n5. Atravesse a Planície dos Fantasmas.', '\n6. Escale a Montanha Nebulosa'])
        escolha = input('Qual caminho você deseja continuar: ')
        return escolha
      elif escolha_segunda_trilha == '3':
        digitando_mensagem('Você opta por explorar a Caverna Escura.')
        time.sleep(2)
        digitando_mensagem(['\n7. Desbrave as Profundezas Sombrias.', '\n8. Enfrente os Morcegos da Escuridão.', '\n9. Siga a luz fraca à distância.'])
        escolha = input('Qual caminho você deseja continuar: ')
        return escolha
      elif escolha_segunda_trilha == '4':
        digitando_mensagem('Você segue a Trilha dos Luminescentes.')
        time.sleep(2)
        digitando_mensagem(['\n10. Investigue as flores brilhantes.', '\n11. Passe pelos Túneis de Cristal.', '\n12. Fuja dos Esporos Venenosos.'])
        escolha = input('Qual caminho você deseja continuar: ')
        return escolha

def terceira_trilha(escolha_terceira_trilha):
    mensagem_final = [
        'Uma reviravolta inesperada! Você precisa voltar ao incício para tentar novamente.',
        'Você encontrou a Cenoura Sagara!!! \n Parabéns, coelho vitorioso!',
        'Oh não!!! Você se depara com criaturas mágica extremamente fortes e elas te atacam e você não sobrevive.'
    ]
    if escolha_terceira_trilha == '1':
        digitando_mensagem('Você segue a trilha de flores mágicas.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '2':
        digitando_mensagem('Você subiu na árvore gigante.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '3':
        digitando_mensagem('Você desvia do riacho encantado.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '4':
        digitando_mensagem('Você desce para a Caverna Subaquática.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '5':
        digitando_mensagem('Você atravessa a Planície dos Fantasmas.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '6':
        digitando_mensagem('Você escala a Montanha Nebulosa.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '7':
        digitando_mensagem('Você desbrava as Profundezas Sombrias.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '8':
        digitando_mensagem('Você enfrenta os Morcegos da Escuridão.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '9':
        digitando_mensagem('Você segue a luz fraca à distância.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '10':
        digitando_mensagem('Você investiga as flores brilhantes.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '11':
        digitando_mensagem('Você passa pelos Túneis de Cristal.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '12':
        digitando_mensagem('Você foge dos Esporos Venenosos.')
        time.sleep(2)
        digitando_mensagem(random.choice(mensagem_final))
    elif escolha_terceira_trilha == '13':
        digitando_mensagem('Isso foi bastante triste.')
        time.sleep(2)
    else:
        digitando_mensagem('Opção inválida. Por favor, escolha uma opção válida.')

def main():
    obter_jogador = nome_jogador()
    mensagem_inicial(obter_jogador)

    rota_escolhida = escolher_rota_inicial()
    primeira_escolha = primeira_trilha(rota_escolhida)
    segunda_escolha = segunda_trilha(primeira_escolha)
    terceira_trilha(segunda_escolha)

if __name__ == '__main__':
    main()