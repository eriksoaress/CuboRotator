import pygame
import numpy as np
FPS = 60  # Frames per Second
clock = pygame.time.Clock()


def inicializa():
    # Inicializa o Pygame
    pygame.init()
    window = pygame.display.set_mode((720, 720), flags=pygame.SCALED)
    cubo = np.array([[100,100,100,1],[100,-100,100,1],[-100,-100,100,1],[-100,100,100,1],[100,100,300,1],[100,-100,300,1],[-100,-100,300,1],[-100,100,300,1]])
    states={"angulo_X":0, 'd': 200, 'posicao_mouse':(0,0), 'aux': (0,0), 'angulo_Y':0, 'angulo_Z': 0, 'rodando': True, 'cubo_x':100, 'cubo_y':100, 'cubo_z':200, 'lado_cubo':200, 'h': 0, 'left': False, 
            'd': 200, 'l':False, 'angulo2': 0.01, 'cubo': cubo, 'last_mouse_pos': pygame.mouse.get_pos(), 'right': False, 'down':False, 'up':False}
  

   

    
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
    
    pontos_cubo = states['cubo']
    if states['right']:
        pontos_cubo =  pontos_cubo@ rotacao_Y(0.04)
        states['cubo'] = pontos_cubo
        states['right'] = False
    
    # if states['down']:
    #     pontos_cubo =  pontos_cubo@ rotacao_X(0.02)
    #     states['cubo'] = pontos_cubo
    #     states['down'] = False
    
    # if states['up']:
    #     pontos_cubo =  pontos_cubo@ rotacao_X(-0.02)
    #     states['cubo'] = pontos_cubo
    #     states['up'] = False
    


    if states['left']:
        pontos_cubo =  pontos_cubo@ rotacao_Y(-0.04)
        states['cubo'] = pontos_cubo
        states['left'] = False


    
    pontos_cubo =  translacao_pra_origem(200,200)@ pontos_cubo.T
    pontos_cubo =  rotacao_Y(states["angulo_Y"]) @ pontos_cubo
    pontos_cubo =  rotacao_X(states["angulo_X"]) @ pontos_cubo
    pontos_cubo =  np.linalg.inv(translacao_pra_origem(200,200))@ pontos_cubo

    translacao = np.array([[1,0,0,360],[0,1,0,360],[0,0,1,0],[0,0,0,1]])
  
    contador  = 0
    for j in range(8):
        if pontos_cubo[2][j] <= 0:
            contador += 1
            pontos_cubo[2][j] = 10
  
    pontos_projecao = matrizP(states['d'])@ pontos_cubo 
    pontos_projecao = translacao@ pontos_projecao
    
    if contador != 8:

        for i in range(0,3):
            pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i]/pontos_projecao[3][i] , pontos_projecao[1][i]/pontos_projecao[3][i]), ( pontos_projecao[0][i + 1]/pontos_projecao[3][i + 1] , pontos_projecao[1][i + 1]/pontos_projecao[3][i + 1]), 4)
            pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i + 4]/pontos_projecao[3][i + 4] , pontos_projecao[1][i + 4]/pontos_projecao[3][i + 4]), ( pontos_projecao[0][i + 5]/pontos_projecao[3][i + 5] , pontos_projecao[1][i + 5]/pontos_projecao[3][i + 5]), 4)
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][3]/pontos_projecao[3][3] , pontos_projecao[1][3]/pontos_projecao[3][3]), ( pontos_projecao[0][0]/pontos_projecao[3][0] , pontos_projecao[1][0]/pontos_projecao[3][0]), 3)
        pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][7]/pontos_projecao[3][7] , pontos_projecao[1][7]/pontos_projecao[3][7]), ( pontos_projecao[0][4]/pontos_projecao[3][4] , pontos_projecao[1][4]/pontos_projecao[3][4]), 3)

        for i in range(4):
            pygame.draw.line(window, (255, 0, 0), ( pontos_projecao[0][i]/pontos_projecao[3][i] , pontos_projecao[1][i]/pontos_projecao[3][i]), ( pontos_projecao[0][i + 4]/pontos_projecao[3][i + 4] , pontos_projecao[1][i + 4]/pontos_projecao[3][i + 4]), 4)
        
    pygame.display.update()

def atualiza_estado(states):  
    # Verifica eventos do Pygame
    if states['rodando']:
        states['angulo_X'] += 0.001
        states['angulo_Y'] += 0.001

    for ev in pygame.event.get():
        # Verifica se o usuário clicou no botão "X" para fechar a janela
        if ev.type == pygame.QUIT:
            return False

        if ev.type == pygame.MOUSEBUTTONDOWN :
            states['posicao_mouse'] = pygame.mouse.get_pos()
            states['rodando'] = False
         

            print(states['posicao_mouse'])
        if ev.type == pygame.MOUSEBUTTONUP:
            states['aux'] = (states['angulo_X'], states['angulo_Y'])  
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            states['cubo'][:,0] -= 10
        if keys[pygame.K_d]:
            states['cubo'][:,0] += 10
        if keys[pygame.K_w]:
            states['cubo'][:,2] -= 10
        if keys[pygame.K_s]:
            states['cubo'][:, 2] += 10
          
       
        

            
           
       

    mouse = pygame.mouse.get_pos()
    dfx = mouse[0] - states['posicao_mouse'][0]
    dfy = mouse[1] - states['posicao_mouse'][1]
    if pygame.mouse.get_pressed()[0]:
        states['angulo_Y'] =  dfx/700 + states['aux'][1]
        states['angulo_X'] =  -dfy/700 + states['aux'][0]       

        # Verifica se foi pressionada alguma tecla.
    keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_UP]:
    #     states['angulo_X'] += 0.002
    # if keys[pygame.K_DOWN]:
    #     states['angulo_X'] -= 0.002
    # if keys[pygame.K_LEFT]:
    #     states['angulo_Y'] += 0.002
    # if keys[pygame.K_RIGHT]:
    #     states['angulo_Y'] -= 0.002
    # if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
    #     if states['d'] > 0.2:
    #         states['d'] -= 0.2
    # if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
    #     states['d'] += 0.2

    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] < states['last_mouse_pos'][0]:
        states['right'] = True
    if mouse_pos[0] > states['last_mouse_pos'][0]:
        states['left'] = True

    if mouse_pos[1] < states['last_mouse_pos'][1]:
        states['up'] = True
    if mouse_pos[1] > states['last_mouse_pos'][1]:
        states['down'] = True

    
    # if mouse_pos[1] < states['last_mouse_pos'][1]:

    # if mouse_pos[1] < last_mouse_pos[1]:
    #     states['c'] = True
    # if mouse_pos[1] > last_mouse_pos[1]:
    #     states['l'] = True
    states['last_mouse_pos'] = mouse_pos
    

           
       
        
            
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