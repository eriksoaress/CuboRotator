import pygame

FPS = 60  # Frames per Second
clock = pygame.time.Clock()


def inicializa():
    # Inicializa o Pygame
    pygame.init()
    window = pygame.display.set_mode((720, 720), flags=pygame.SCALED)
   

    
    return window



def finaliza():
    '''Função utilizada para fechar o pygame'''
    if pygame.get_init():
        pygame.quit()

def desenha(window: pygame.Surface, assets, state):
    pygame.display.update()

def atualiza_estado(state,assets):
    # Verifica eventos do Pygame
    for ev in pygame.event.get():
        # Verifica se o usuário clicou no botão "X" para fechar a janela
        if ev.type == pygame.QUIT:
            return False

    # Retorna "True" para indicar que o jogo continua em andamento
    return True

def gameloop(window, assets, state):
    while atualiza_estado(state,assets):
        desenha(window, assets, state) 