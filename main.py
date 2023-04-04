import pygame
import numpy as np
FPS = 60  # Frames per Second
clock = pygame.time.Clock()


def inicializa():
    # Inicializa o Pygame
    pygame.init()
    window = pygame.display.set_mode((720, 720), flags=pygame.SCALED)
    states={"angulo_X":0,"angulo_Y":0,"angulo_Z":0, 'd': 200}

   

    
    return window, states


def matrizP(d):
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-1/d,0]])

def rotacao_Z(angulo_Z):
    return np.array([[np.cos(angulo_Z),-np.sin(angulo_Z),0,0],[np.sin(angulo_Z),np.cos(angulo_Z),0,0],[0,0,1,0],[0,0,0,1]])

def rotacao_Y(angulo_Y):
    return np.array([[np.cos(angulo_Y),0,np.sin(angulo_Y),0],[0,1,0,0],[-np.sin(angulo_Y),0,np.cos(angulo_Y),0],[0,0,0,1]])

def rotacao_X(angulo_X):
    return np.array([[1,0,0,0],[0,np.cos(angulo_X),-np.sin(angulo_X),0],[0,np.sin(angulo_X),np.cos(angulo_X),0],[0,0,0,1]])

def translacao_pra_origem(h_cubo, lado_cubo):
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,1,-h_cubo - lado_cubo/2],[0,0,0,1]])

def finaliza():
    '''Função utilizada para fechar o pygame'''
    if pygame.get_init():
        pygame.quit()

def desenha(window: pygame.Surface, states):

  
    window.fill((0, 0, 0))
    
    pontos_cubo = np.array([[100,100,200,1],[100,-100, 200,1],[-100,-100,200,1],[-100,100,200,1], [100,100,400,1],[100,-100,400,1],[-100,-100,400,1],[-100,100,400,1]])
    pontos_cubo =  translacao_pra_origem(200,200)@ pontos_cubo.T
    pontos_cubo =  rotacao_Y(states["angulo_Y"]) @ pontos_cubo
    pontos_cubo =  rotacao_X(states["angulo_X"]) @ pontos_cubo
    pontos_cubo =  np.linalg.inv(translacao_pra_origem(200,200))@ pontos_cubo

    translacao = np.array([[1,0,0,360],[0,1,0,360],[0,0,1,0],[0,0,0,1]])
    pontos_projecao = matrizP(states['d'])@ pontos_cubo 
    pontos_projecao = translacao@ pontos_projecao

   
    for i in range(0,3):
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i]/pontos_projecao[3][i] , pontos_projecao[1][i]/pontos_projecao[3][i]), ( pontos_projecao[0][i + 1]/pontos_projecao[3][i + 1] , pontos_projecao[1][i + 1]/pontos_projecao[3][i + 1]), 3)
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i + 4]/pontos_projecao[3][i + 4] , pontos_projecao[1][i + 4]/pontos_projecao[3][i + 4]), ( pontos_projecao[0][i + 5]/pontos_projecao[3][i + 5] , pontos_projecao[1][i + 5]/pontos_projecao[3][i + 5]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][3]/pontos_projecao[3][3] , pontos_projecao[1][3]/pontos_projecao[3][3]), ( pontos_projecao[0][0]/pontos_projecao[3][0] , pontos_projecao[1][0]/pontos_projecao[3][0]), 3)
    pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][7]/pontos_projecao[3][7] , pontos_projecao[1][7]/pontos_projecao[3][7]), ( pontos_projecao[0][4]/pontos_projecao[3][4] , pontos_projecao[1][4]/pontos_projecao[3][4]), 3)

    for i in range(4):
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i]/pontos_projecao[3][i] , pontos_projecao[1][i]/pontos_projecao[3][i]), ( pontos_projecao[0][i + 4]/pontos_projecao[3][i + 4] , pontos_projecao[1][i + 4]/pontos_projecao[3][i + 4]), 3)
    
    pygame.display.update()

def atualiza_estado(states):  
    # Verifica eventos do Pygame
    for ev in pygame.event.get():
        # Verifica se o usuário clicou no botão "X" para fechar a janela
        if ev.type == pygame.QUIT:
            return False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            diff = 360 - ev.pos[1]
            if diff > 0:
                # Aumenta o valor de d se o mouse foi arrastado para cima
                if states['d'] + 0.2 * diff <= 600:
                    states['d'] += 0.2 * diff
                    print(f'diff: {diff}')
            elif diff < 0:
                # Diminui o valor de d se o mouse foi arrastado para baixo
                if states['d'] + 0.2 * diff >= 30:
                    states['d'] += 0.2 * diff
                    print(f'diff: {diff}')

        # Verifica se foi pressionada alguma tecla.
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        states['angulo_X'] += 0.002
    if keys[pygame.K_DOWN]:
        states['angulo_X'] -= 0.002
    if keys[pygame.K_LEFT]:
        states['angulo_Y'] += 0.002
    if keys[pygame.K_RIGHT]:
        states['angulo_Y'] -= 0.002
    
           
       
        
            
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