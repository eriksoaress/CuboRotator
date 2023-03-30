import pygame
import numpy as np
FPS = 60  # Frames per Second
clock = pygame.time.Clock()


def inicializa():
    # Inicializa o Pygame
    pygame.init()
    window = pygame.display.set_mode((720, 720), flags=pygame.SCALED)
   

    
    return window


def matrizP(d):
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-1/d,0]])



def finaliza():
    '''Função utilizada para fechar o pygame'''
    if pygame.get_init():
        pygame.quit()

def desenha(window: pygame.Surface):

    pontos_cubo =np.array([[100,100,100,1],[100,-100, 100,1],[-100,-100,100,1],[-100,100,100,1], [100,100,300,1],[100,-100,300,1],[-100,-100,300,1],[-100,100,300,1]])
    pontos_projecao = pontos_cubo @ np.linalg.inv(matrizP(100))
    print(pontos_projecao)
    xp = pontos_projecao[:,0]/pontos_projecao[:,3]
    yp = pontos_projecao[:,1]/pontos_projecao[:,3]
    
    print("yp: ", yp)
    print("xp: ", xp)
 
    


    pygame.draw.line(window, (255, 0, 0), (xp[0], yp[0]), (xp[1], yp[1]), 1)
    pygame.draw.line(window, (255, 0, 0), (xp[1], yp[1]), (xp[2], yp[2]), 1)
    pygame.display.update()

def atualiza_estado():  
    # Verifica eventos do Pygame
    for ev in pygame.event.get():
        # Verifica se o usuário clicou no botão "X" para fechar a janela
        if ev.type == pygame.QUIT:
            return False
   
    


    # Retorna "True" para indicar que o jogo continua em andamento
    return True

def gameloop(window):
    while atualiza_estado():
        desenha(window) 


if __name__ == '__main__':
    window = inicializa()
    gameloop(window)
    finaliza()