# CuboRotator
Cubo Rotator é um programa que permite visualizar e interagir com um cubo através da biblioteca de interface gráfica Pygame.

## Instalação
Para utilizar o programa basta clonar esse repositório em algum local de sua máquina. Para fazer isso, clique no botão verde **"Code"** logo acima, escolha um modo de baixar o repositório, podendo ser baixando o zip e descompactando ou clonando através de https ou ssh. Após seguir essas etapas, será preciso instalar as bibliotecas necessárias. Isso pode ser feito, estando na raiz do projeto, rodando no terminal o seguinte comando:  `pip install -r requirements.txt `, com isso, as bibliotecas necessárias serão instaladas. Com a instalação feita e na pasta raiz do projeto, basta executar o seguinte comando para rodar o programa: `python  .\main.py `( ou `python3 .\main.py`, dependendo da sua versão instalada do python).

## Modelo matemático
Para criar o cubo foi necessário, primeiramente, encontrar a matriz tranformação que nos permite encontrar as projeções dos vértices do cubo quando alteramos o valor para um eixo. Para isso realizamos os procedimentos expostos na imagem abaixo:
