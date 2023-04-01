import pygame
import numpy as np
FPS = 60  # Frames per Second
clock = pygame.time.Clock()


def inicializa():
    # Inicializa o Pygame
    pygame.init()
    window = pygame.display.set_mode((720, 720), flags=pygame.SCALED)
    states={"angulo":0}

   

    
    return window, states


def matrizP(d):
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-1/d,0]])

def rotacao(angulo):
    return np.array([[np.cos(angulo),-np.sin(angulo),0,0],[np.sin(angulo),np.cos(angulo),0,0],[0,0,1,0],[0,0,0,1]])



def finaliza():
    '''Função utilizada para fechar o pygame'''
    if pygame.get_init():
        pygame.quit()

def desenha(window: pygame.Surface, states):

  
    window.fill((0, 0, 0))
    pontos_cubo =np.array([[100,100,100,1],[100,-100, 100,1],[-100,-100,100,1],[-100,100,100,1], [100,100,300,1],[100,-100,300,1],[-100,-100,300,1],[-100,100,300,1]])
    translacao = np.array([[1,0,0,200],[0,1,0,200],[0,0,1,0],[0,0,0,1]])
    pontos_projecao = matrizP(100)@pontos_cubo.T
    pontos_projecao = rotacao(states['angulo'])@pontos_projecao
    pontos_projecao = translacao@pontos_projecao

    print(pontos_projecao)
    for i in range(0,3):
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i]/pontos_projecao[3][i] , pontos_projecao[1][i]/pontos_projecao[3][i]), ( pontos_projecao[0][i + 1]/pontos_projecao[3][i + 1] , pontos_projecao[1][i + 1]/pontos_projecao[3][i + 1]), 3)
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i + 4]/pontos_projecao[3][i + 4] , pontos_projecao[1][i + 4]/pontos_projecao[3][i + 4]), ( pontos_projecao[0][i + 5]/pontos_projecao[3][i + 5] , pontos_projecao[1][i + 5]/pontos_projecao[3][i + 5]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][3]/pontos_projecao[3][3] , pontos_projecao[1][3]/pontos_projecao[3][3]), ( pontos_projecao[0][0]/pontos_projecao[3][0] , pontos_projecao[1][0]/pontos_projecao[3][0]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][7]/pontos_projecao[3][7] , pontos_projecao[1][7]/pontos_projecao[3][7]), ( pontos_projecao[0][4]/pontos_projecao[3][4] , pontos_projecao[1][4]/pontos_projecao[3][4]), 3)

    for i in range(4):
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i]/pontos_projecao[3][i] , pontos_projecao[1][i]/pontos_projecao[3][i]), ( pontos_projecao[0][i + 4]/pontos_projecao[3][i + 4] , pontos_projecao[1][i + 4]/pontos_projecao[3][i + 4]), 3)
    
 
    

    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][0]/pontos_projecao[2][0] , pontos_projecao[1][0]/pontos_projecao[2][0]), ( pontos_projecao[0][1]/pontos_projecao[2][1],  pontos_projecao[1][1]/pontos_projecao[2][1]), 3)
    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][1]/pontos_projecao[2][1] , pontos_projecao[1][1]/pontos_projecao[2][1]), ( pontos_projecao[0][2]/pontos_projecao[2][2] , pontos_projecao[1][2]/pontos_projecao[2][2]), 3)
    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][2]/pontos_projecao[2][2] , pontos_projecao[1][2]/pontos_projecao[2][2]), ( pontos_projecao[0][3]/pontos_projecao[2][3] , pontos_projecao[1][3]/pontos_projecao[2][3]), 3)
    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][3]/pontos_projecao[2][3] , pontos_projecao[1][3]/pontos_projecao[2][3]), ( pontos_projecao[0][0]/pontos_projecao[2][0] , pontos_projecao[1][0]/pontos_projecao[2][0]), 3)

    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][4]/pontos_projecao[2][4] , pontos_projecao[1][4]/pontos_projecao[2][4]),  (pontos_projecao[0][5]/pontos_projecao[2][5],  pontos_projecao[1][5]/pontos_projecao[2][5]), 3)
    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][5]/pontos_projecao[2][5] , pontos_projecao[1][5]/pontos_projecao[2][5]), ( pontos_projecao[0][6]/pontos_projecao[2][6] , pontos_projecao[1][6]/pontos_projecao[2][6]), 3)
    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][6]/pontos_projecao[2][6] , pontos_projecao[1][6]/pontos_projecao[2][6]), ( pontos_projecao[0][7]/pontos_projecao[2][7] , pontos_projecao[1][7]/pontos_projecao[2][7]), 3)
    # pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][7]/pontos_projecao[2][7] , pontos_projecao[1][7]/pontos_projecao[2][7]), ( pontos_projecao[0][4]/pontos_projecao[2][4] , pontos_projecao[1][4]/pontos_projecao[2][4]), 3)

    pygame.display.update()

def atualiza_estado(states):  
    # Verifica eventos do Pygame
    for ev in pygame.event.get():
        # Verifica se o usuário clicou no botão "X" para fechar a janela
        if ev.type == pygame.QUIT:
            return False
        
        # Verifica se foi pressionada alguma tecla.
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        states['angulo'] += 0.001
    if keys[pygame.K_RIGHT]:
        states['angulo'] -= 0.001

           
       
        
            
            # Dependendo da tecla, altera a velocidade.
            
 
   
    


    # Retorna "True" para indicar que o jogo continua em andamento
    return True

def gameloop(window,states):
    while atualiza_estado(states):
        desenha(window,states) 


if __name__ == '__main__':
    window , states= inicializa()
    gameloop(window,states)
    finaliza()