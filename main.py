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
    translacao = np.array([[1,0,360,0],[0,1,360,0],[0,0,1,0]])
    pontos_projecao = matrizP(1)@pontos_cubo.T
    pontos_projecao = translacao@pontos_projecao
    print(pontos_projecao)
    

    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][0]/pontos_projecao[2][0] , pontos_projecao[1][0]/pontos_projecao[2][0]), ( pontos_projecao[0][1]/pontos_projecao[2][1],  pontos_projecao[1][1]/pontos_projecao[2][1]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][1]/pontos_projecao[2][1] , pontos_projecao[1][1]/pontos_projecao[2][1]), ( pontos_projecao[0][2]/pontos_projecao[2][2] , pontos_projecao[1][2]/pontos_projecao[2][2]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][2]/pontos_projecao[2][2] , pontos_projecao[1][2]/pontos_projecao[2][2]), ( pontos_projecao[0][3]/pontos_projecao[2][3] , pontos_projecao[1][3]/pontos_projecao[2][3]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][3]/pontos_projecao[2][3] , pontos_projecao[1][3]/pontos_projecao[2][3]), ( pontos_projecao[0][0]/pontos_projecao[2][0] , pontos_projecao[1][0]/pontos_projecao[2][0]), 3)

    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][4]/pontos_projecao[2][4] , pontos_projecao[1][4]/pontos_projecao[2][4]),  (pontos_projecao[0][5]/pontos_projecao[2][5],  pontos_projecao[1][5]/pontos_projecao[2][5]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][5]/pontos_projecao[2][5] , pontos_projecao[1][5]/pontos_projecao[2][5]), ( pontos_projecao[0][6]/pontos_projecao[2][6] , pontos_projecao[1][6]/pontos_projecao[2][6]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][6]/pontos_projecao[2][6] , pontos_projecao[1][6]/pontos_projecao[2][6]), ( pontos_projecao[0][7]/pontos_projecao[2][7] , pontos_projecao[1][7]/pontos_projecao[2][7]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][7]/pontos_projecao[2][7] , pontos_projecao[1][7]/pontos_projecao[2][7]), ( pontos_projecao[0][4]/pontos_projecao[2][4] , pontos_projecao[1][4]/pontos_projecao[2][4]), 3)

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