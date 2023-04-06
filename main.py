# Importando as bibliotecas necessárias
import pygame
import numpy as np

FPS = 60  # Frames por Segundo
clock = pygame.time.Clock()


# Função que inicializa o jogo
def inicializa():
    # Inicializando o Pygame
    pygame.init()

    # Criando a janela principal do jogo
    window = pygame.display.set_mode((720, 720), flags=pygame.SCALED)

    # Definindo os pontos do cubo
    cubo = np.array([[100, 100, 200, 1],[100, -100, 200, 1],[-100, -100, 200, 1],[-100, 100, 200, 1],[100, 100, 400, 1],[100, -100, 400, 1],[-100, -100, 400, 1],[-100, 100, 400, 1]])

    # Definindo os estados iniciais do jogo
    states = {"angulo_X": 0,"d": 200,"posicao_mouse": (0, 0),"aux": (0, 0),"angulo_Y": 0,"angulo_Z": 0,
              "rodando": True,"cubo_x": 100,"cubo_y": 100,"cubo_z": 200,"lado_cubo": 200,"h": 0,"left": False,
              "d": 200,"l": False,"angulo2": 0.01,"cubo": cubo,"last_mouse_pos": pygame.mouse.get_pos(),
              "right": False,"down": False,"up": False
    }
    return window, states


# Função que define a matriz de projeção
def matrizP(d):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, -d],
        [0, 0, -1 / d, 0]
    ])


# Função que define a rotação em torno do eixo Z
def rotacao_Z(angulo_Z):
    return np.array([[np.cos(angulo_Z), -np.sin(angulo_Z), 0, 0],[np.sin(angulo_Z), np.cos(angulo_Z), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])

# Função que define a rotação em torno do eixo Y
def rotacao_Y(angulo_Y):
    return np.array([[np.cos(angulo_Y), 0, np.sin(angulo_Y), 0],[0, 1, 0, 0],[-np.sin(angulo_Y), 0, np.cos(angulo_Y), 0],[0, 0, 0, 1]])

# Função que define a rotação em torno do eixo X
def rotacao_X(angulo_X):
    return np.array([[1,0,0,0],[0,np.cos(angulo_X),-np.sin(angulo_X),0],[0,np.sin(angulo_X),np.cos(angulo_X),0],[0,0,0,1]])

# Define a translação para a origem
def translacao_pra_origem():
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,1,-300],[0,0,0,1]])



    
def finaliza():
    '''Função utilizada para fechar o pygame'''
    if pygame.get_init():
        pygame.quit()

def desenha(window: pygame.Surface, states):
    
    # Preenche a janela com a cor preta
    window.fill((0, 0, 0))
    
    # Obtém os pontos do cubo a partir do estado atual
    pontos_cubo = states['cubo']
    
    # Se a tecla 'right' foi pressionada e o cubo não está girando, rotaciona o cubo em torno do eixo y
    if states['right'] and not(states['rodando']) :
        pontos_cubo = pontos_cubo @ rotacao_Y(0.04)
        states['cubo'] = pontos_cubo
        states['right'] = False
    
    # Se a tecla 'left' foi pressionada e o cubo não está girando, rotaciona o cubo em torno do eixo y
    if states['left']:
        pontos_cubo = pontos_cubo @ rotacao_Y(-0.04)
        states['cubo'] = pontos_cubo
        states['left'] = False
    
    # Aplica as transformações de rotação e translação nos pontos do cubo
    pontos_cubo = translacao_pra_origem() @ pontos_cubo.T
    pontos_cubo = rotacao_Y(states["angulo_Y"]) @ pontos_cubo
    pontos_cubo = rotacao_X(states["angulo_X"]) @ pontos_cubo
    pontos_cubo = np.linalg.inv(translacao_pra_origem()) @ pontos_cubo
    
    # Define a matriz de translação que será utilizada para projetar os pontos do cubo na tela
    translacao = np.array([[1, 0, 0, 360], [0, 1, 0, 360], [0, 0, 1, 0], [0, 0, 0, 1]])
  
    # Define um contador que será utilizado para verificar se o cubo está sendo projetado atrás da tela
    contador = 0
    
    # Verifica se algum dos pontos do cubo está sendo projetado atrás da tela e, se sim, adiciona 1 ao contador
    for j in range(8):
        if pontos_cubo[2][j] <= 0:
            contador += 1
            pontos_cubo[2][j] = 10
  
    # Projeta os pontos do cubo na tela
    pontos_projecao = matrizP(states['d']) @ pontos_cubo 
    pontos_projecao = translacao @ pontos_projecao
    
    # Desenha as linhas do cubo
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

        # Verifica se o usuário clicou com o mouse
        if ev.type == pygame.MOUSEBUTTONDOWN :
            if ev.button == 1:
                states['posicao_mouse'] = pygame.mouse.get_pos()
                if states['rodando']:
                    states['rodando'] = False
                else:
                    states['rodando'] = True
                    states['cubo'] = np.array([[100, 100, 200, 1],[100, -100, 200, 1],[-100, -100, 200, 1],[-100, 100, 200, 1],[100, 100, 400, 1],[100, -100, 400, 1],[-100, -100, 400, 1],[-100, 100, 400, 1]])

        

        # Verifica se o usuário apertou em alguma das seguintes teclas: ASDW, para mover o personagem dentro do plano
        keys = pygame.key.get_pressed()
        if not states['rodando']:
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
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if not states['rodando']:
                # Verifique se o botão do mouse é o scroll para cima
                if ev.button == 4:
                    if states['d'] + 5 <= 600:
                        states['d'] += 5
                # Verifique se o botão do mouse é o scroll para baixo
                elif ev.button == 5:
                    if states['d'] - 5 >= 30:
                        states['d'] -= 5

        # Verifica se foi pressionada alguma tecla.
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    # Verificações para ver se o mouse está se movendo
    if not states['rodando']:
        if mouse_pos[0] < states['last_mouse_pos'][0]:
            states['right'] = True
        if mouse_pos[0] > states['last_mouse_pos'][0]:
            states['left'] = True
        states['last_mouse_pos'] = mouse_pos

    # Retorna "True" para indicar que o jogo continua em andamento
    return True

def gameloop(window,states):
    while atualiza_estado(states):
        desenha(window,states) 


if __name__ == '__main__':
    window , states= inicializa()
    gameloop(window,states)
    finaliza()