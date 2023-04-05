# CuboRotator
Cubo Rotator é um programa que permite visualizar e interagir com um cubo através da biblioteca de interface gráfica Pygame.

## Instalação
Para utilizar o programa basta clonar esse repositório em algum local de sua máquina. Para fazer isso, clique no botão verde **"Code"** logo acima, escolha um modo de baixar o repositório, podendo ser baixando o zip e descompactando ou clonando através de https ou ssh. Após seguir essas etapas, será preciso instalar as bibliotecas necessárias. Isso pode ser feito, estando na raiz do projeto, rodando no terminal o seguinte comando:  `pip install -r requirements.txt `, com isso, as bibliotecas necessárias serão instaladas. Com a instalação feita e na pasta raiz do projeto, basta executar o seguinte comando para rodar o programa: `python  .\main.py `( ou `python3 .\main.py`, dependendo da sua versão instalada do python).

## Modelo matemático
Para criar o cubo foi necessário, primeiramente, encontrar a matriz tranformação que nos permite projetar os vértices de um cubo que possui 3 dimensões em um plano 2D que no caso é a tela do pygame. Para isso realizamos os procedimentos expostos na imagem abaixo:

Primeiro, fixamos o eixo y e trabalhamos apenas com o eixo x e z, projetando o ponto através do orifício e alcançando o pinhole que se encontra a uma distância 'd' da origem
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/desenho_plano.jpg">
\
Após isso, utilizamos semelhança de triângulo para obter uma relação entre ambos os pontos
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/tan.jpg">
\
Fizemos manipulações e operações matemáticas e chegamos em uma equação simplificada com x0 e xp
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/x0_inicial.jpg">
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/wp.jpg">
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/x0_simplificado.jpg">
\
Depois de todos esses procedimentos, conseguimos escrever essas equações em forma de matriz para trabalhar mais facilmente com python
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/xp_matriz.jpg">
\
Realizamos todos esses passos para chegar em uma matriz que nos ajuda a encontrar o ponto xp, mas precisamos realizar todos os pontos novamente, mas dessa vez fixando o eixo x e trabalhando com y e z para obter a matriz que nos ajuda a encontrar o ponto yp. Haja vista que os passos são semelhantes, mostraremos apenas o resultado obtido abaixo.
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/yp_matriz.jpg">
\
Por fim, podemos juntar as duas matrizes, haja vista que ambas dependem do mesmo zp, com o intuito de utilizar o resultado para nos auxiliar nas projeções dos vértices do cubo
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/matriz_final.jpg">

Com a matriz P pronta, definimos os pontos iniciais dos vértices do cubo, o ângulo de cada eixo, e a distância focal (d). Transladamos o cubo para a origem para trabalhar com ele através da matriz [[1,0,0,0],[0,1,0,0],[0,0,1,-h_cubo - lado_cubo/2],[0,0,0,1]], rotacionamos o cubo em relação ao eixo x e y de acordo com os seus ângulos através das matrizes [[1,0,0,0],[0,np.cos(angulo_X),-np.sin(angulo_X),0],[0,np.sin(angulo_X),np.cos(angulo_X),0],[0,0,0,1]] e [np.cos(angulo_Y),0,np.sin(angulo_Y),0],[0,1,0,0],[-np.sin(angulo_Y),0,np.cos(angulo_Y),0],[0,0,0,1]], após fazermos uma pré-multiplicação com essas matrizes de rotação, retornamos o cubo para o centro da tela pré-multiplicando pela inversa da matriz utilizada anteriormente para leva-la para a origem.
\
Com todas as translações e rotações necessárias inicialmente, podemos utilizar a nossa matriz P pré multiplicando os pontos do cubo para projetar esses pontos no plano 3d.
\
A aplicação também permite que o usuário altere a distância focal do cubo, fazendo com que ele fique maior ou menor, a depender da ação do usuário nós alteramos o valor do 'd', sendo que diminuimos ele para deixar o cubo menor e aumentamos o 'd' para deixar o cubo maior.






## Como utilizar
Inicialmente, o cubo já estará girando, porém, é possível também interagir com ele através do mouse, caso o usuário role o scroll do mouse para baixo o cubo ficará maior, e caso role para cima o cubo ficará menor.
