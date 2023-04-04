# CuboRotator
Cubo Rotator é um programa que permite visualizar e interagir com um cubo através da biblioteca de interface gráfica Pygame.

## Instalação
Para utilizar o programa basta clonar esse repositório em algum local de sua máquina. Para fazer isso, clique no botão verde **"Code"** logo acima, escolha um modo de baixar o repositório, podendo ser baixando o zip e descompactando ou clonando através de https ou ssh. Após seguir essas etapas, será preciso instalar as bibliotecas necessárias. Isso pode ser feito, estando na raiz do projeto, rodando no terminal o seguinte comando:  `pip install -r requirements.txt `, com isso, as bibliotecas necessárias serão instaladas. Com a instalação feita e na pasta raiz do projeto, basta executar o seguinte comando para rodar o programa: `python  .\main.py `( ou `python3 .\main.py`, dependendo da sua versão instalada do python).

## Modelo matemático
Para criar o cubo foi necessário, primeiramente, encontrar a matriz tranformação que nos permite encontrar as projeções dos vértices do cubo quando alteramos o valor para um eixo. Para isso realizamos os procedimentos expostos na imagem abaixo:

Primeiro, fixamos o eixo y e trabalhamos apenas com o eixo x e z, projetando o ponto através do orifício e alcançando o pinhole que se encontra a uma distância 'd' da origem
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/desenho_plano.jpg">

Após isso, utilizamos semelhança de triângulo para obter uma relação entre ambos os pontos
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/tan.jpg">
Fizemos manipulações e operações matemáticas e chegamos em uma equação simplificada com x0 e xp
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/x0_inicial.jpg">
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/wp.jpg">
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/x0_simplificado.jpg">
Depois de todos esses procedimentos, conseguimos escrever essas equações em forma de matriz para trabalhar mais facilmente com python
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/xp_matriz.jpg">
Realizamos todos esses passos para chegar em uma matriz que nos ajuda a encontrar o ponto xp, mas precisamos realizar todos os pontos novamente, mas dessa vez ficando o eixo x e obtendo a matriz que nos ajuda a encontrar o ponto yp
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/yp_matriz.jpg">
Por fim, podemos juntar as duas matrizes, haja vista que ambas dependem do mesmo zp, com o intuito de utilizar o resultado para nos auxiliar nas projeções dos vértices do cubo
<img src= "https://github.com/eriksoaress/CuboRotator/blob/main/matriz_final.jpg">







## Como utilizar
Inicialmente, o cubo já estará girando, porém, é possível também interagir com ele através do mouse, caso clique na metade superior da tela o cubo ficará maior, e caso clique na metade inferior da tela o cubo ficará menor. Além disso, as teclas seta para cima, para baixo, direita, e esquerda, permitem alterar o ângulo de visuaização do cubo da forma que tiver interesse.