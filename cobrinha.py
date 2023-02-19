"""

"""
# Imports =============================================================================================================

import pygame
from pygame.locals import *  # Significa que importamos todas funções e constantes contidas em pygame.locals
from sys import exit  # Função para fechar janela
from random import randint

pygame.init()  # Primeiro código, para inicializar a biblioteca pygame

# Fonte =============================================================================================================

fonte = pygame.font.SysFont('arial', 20, True, True)
# Fonte, parametros: ('fonte', tamanho, negrito(true or false), italico(true or false))

pontos = 0

# Sons =============================================================================================================

musica_fundo = pygame.mixer.music.load('C:\\Users\\marco\\PycharmProjects\\PyGame\\sons\\BoxCat Games - Victory.mp3')
# carregar a música em uma variável

pygame.mixer.music.set_volume(0.1)  # função para setar o volume da música de fundo entre 0 e 1

pygame.mixer.music.play(-1)  # tocar a música carregada (-1) para loop

barulho_colisao = pygame.mixer.Sound('C:\\Users\\marco\\PycharmProjects\\PyGame\\sons\\smw_coin.wav')

barulho_colisao.set_volume(1)

# Variáveis posicionais ===============================================================================================

largura_tela = 640
altura_tela = 480

velocidade = 1
x_controle = velocidade  # variaveis para ir adcionando a cada iteração do loop
y_controle = 0           # fazendo com que tenha a ideia de que está se movimentando sem parar

x_cobra = largura_tela / 2  # Variável para controlar a posição da cobra no eixo x
y_cobra = altura_tela / 2  # Variável para controlar a posição da cobra no eixo y

x_comida = randint(30, 610)  # posição da comida aleatória x e y
y_comida = randint(30, 450)

# Tela =============================================================================================================

tela = pygame.display.set_mode((largura_tela, altura_tela))  # largura e altura da janela
pygame.display.set_caption('Testando')  # Definir título da janela

relogio = pygame.time.Clock()  # Objeto para controlar os frames da janela

# Função para reiniciar o jogo ========================================================================================
morreu = False


def reiniciar_jogo():  # Reiniciaremos cada comando inicial nesta função

    global pontos, comprimento_corpo, x_comida, y_comida, x_cobra, y_cobra, lista_cabeca, lista_corpo, morreu
    # Tornar as variáveis globais para poder alterar

    pontos = 0
    comprimento_corpo = 0
    x_comida = randint(30, 610)
    y_comida = randint(30, 450)
    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2
    lista_cabeca = []
    lista_corpo = []
    morreu = False

# Função Crescer Cobra ================================================================================================
lista_corpo = []
comprimento_corpo = 0


def crescer(lista_corpo):

    # Função para fazer o corpo da cobra crescer, adicionando no seu corpo a última coordenada da cabeça
    for XeY in lista_corpo:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, (0, 235, 90), (XeY[0], XeY[1], 20, 20))


# Rodar =============================================================================================================
while True:  # Loop para rodar o game

    relogio.tick(200)  # Parametro: FPS # serve para controlar a velocidade dos movimentos

    tela.fill((255, 255, 255))  # preenchimento do background da tela

    mensagem = f'pontos: {pontos}'  # mensagem

    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))  # formatar a mensagem
    # parametros: (mensagem, nao_serrilhado(True or False), (r, g, b))

    for event in pygame.event.get():  # Loop para detectar se algum evento ocorre

        if event.type == QUIT:  # If para fechar a janela
            pygame.quit()
            exit()

        if event.type == KEYDOWN:  # Caso determinada tecla for clicada para baixo fazer:

            if event.key == K_a:  # tecla a
                if x_controle == velocidade:  # If para não permitir que a cobra ande para +X e -X ao mesmo tempo
                    pass                      # se x_controle estiver a ir para direita é para passar e nao permitir ir
                                              # para esquerda
                else:
                    x_controle = -velocidade  # definir a variável x_controle que será adicionada a cada iteração do
                    y_controle = 0            # loop na variável de coordenada do objeto cobra (x_cobra e y_cobra)

            if event.key == K_d:  # tecla d
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:  # tecla w
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade

            if event.key == K_s:  # tecla s
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra += x_controle  # Adicionares as coordenadas da cobra a variavel de controle do eixo x
    y_cobra += y_controle  # Adicionares as coordenadas da cobra a variavel de controle do eixo y

    cobra = pygame.draw.rect(tela, (0, 255, 90), (x_cobra, y_cobra, 20, 20))  # objeto da cobra conforme as suas
                                                                              # variáveis de coordenada

    comida = pygame.draw.circle(tela, (255, 90, 0), (x_comida, y_comida), 10)  # objeto da comida conforme
                                                                               # suas coordenadas aleatórias

    """
    if pygame.key.get_pressed()[K_a]:  # Se a tecla (que está entre []) for pressionado fazer:
        x_cobra -= velocidade

        if x_cobra <= 0:  # "travar" o limite esquerdo da tela
            x_cobra = 0

    if pygame.key.get_pressed()[K_d]:  # Se a tecla (que está entre []) for pressionado fazer:
        x_cobra += velocidade

        if x_cobra >= 620:  # "travar" o limite direito da tela
            x_cobra = 620

    if pygame.key.get_pressed()[K_w]:  # Se a tecla (que está entre []) for pressionado fazer:
        y_cobra -= velocidade

        if y_cobra <= 35:  # "travar" o limite superior da tela
            y_cobra = 35

    if pygame.key.get_pressed()[K_s]:  # Se a tecla (que está entre []) for pressionado fazer:
        y_cobra += velocidade

        if y_cobra >= 460:  # "travar" o limite inferior da tela
            y_cobra = 460
    """

    if cobra.colliderect(comida):  # comando para verificar se houve colisão em um retangulo # parametro: objeto comida
        x_comida = randint(30, 610)
        y_comida = randint(30, 450)
        pontos += 1
        barulho_colisao.play()
        comprimento_corpo += 20

    # adicionar a lista da cabeça o último valor das coordenadas da cobra (x_cobra, y_cobra)
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    # adicionar a lista do corpo da cobra as últimas posições do objeto cabeça
    lista_corpo.append(lista_cabeca)

    if lista_corpo.count(lista_cabeca) > 1:  # função count serve para nos mostrar quantas informações iguais ao
                                             # parametro (lista_cabeça) há dentro da lista_corpo, ou seja,
                                             # se a cobra encostar em si mesma

        fonte2 = pygame.font.SysFont('arial', 20, bold=True, italic=True)
        mensagem_gameover = 'Game Over! Aperte a tecla "R" para começar de novo.'
        texto_formatado_gameover = fonte2.render(mensagem_gameover, True, (0, 0, 0))

        ret_texto = texto_formatado_gameover.get_rect()  # Comando para pegar o retangulo do texto

        morreu = True
        while morreu:

            tela.fill((255, 255, 255))  # deixar a tela toda branca ao morrer

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:  # se apertar r quando morreu = True: é para função reiniciar_jogo() acontecer
                        reiniciar_jogo()

            ret_texto.center = (largura_tela//2, altura_tela//2)  # definer o retangulo do texto com .center para pegar
                                                                  # o centro do retanguloe colocalo em determinada
                                                                  # coordenada

            tela.blit(texto_formatado_gameover, ret_texto)  # colocar na tela o texto formatado na posição do
                                                            # retangulo dele mesmo (ret_texto)
            # Aparecer na tela conforme a coordenada

            pygame.display.update()  # atualizar a tela

    # If's para que a cobra ao ultrapassar um limite da janela, apareça no outro limite
    if x_cobra > largura_tela:
        x_cobra = 0

    if x_cobra < 0:
        x_cobra = largura_tela

    if y_cobra > altura_tela:
        y_cobra = 0

    if y_cobra < 0:
        y_cobra = altura_tela

    if len(lista_corpo) > comprimento_corpo:  # if para excluir a última parte do corpo da cobra de acordo com o seu
        del lista_corpo[0]                    # comprimento alterado pela quantidade de pontuação

    # função crescer para aumentar o objeto
    crescer(lista_corpo)

    tela.blit(texto_formatado, (10, 10))  # Função para adcionar o texto formatado na janela
    # parametros: (texto, (posição x, posição y))

    pygame.display.update()  # Atualização da tela

