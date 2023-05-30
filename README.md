Simulador de colisões:
A ideia do projeto do grupo é desenvolver uma simulação de um gás ideal num modelo de física clássica e sem troca de energia com o exterior, temos como objetivo simular as partículas como bolas de bilhar (massa, área...) que interagem entre si colidindo elasticamente e sem simular as interações intermoleculares (como formações de ligações químicas) a princípio.  

Nosso interesse é desenvolver um programa que permita a visualização e demonstração de conceitos termodinâmicos num gás ideal. Sendo ele composto por partículas independentes, não localizadas e indistinguíveis.

O que foi realizado até então:
Simulamos uma situação com 50 partículas em uma caixa, onde elas colidem elasticamente, até então as bibliotecas vphyton e random foram utilizadas para randomizar as propriedades da classe e o vpython para facilitar a otimização da programação. 
Definimos algumas variáveis de dimensão do sistema, definimos duas listas, uma vazia das bolas que serão criadas no final do prgroama e uma de cores para randomizar nas bolinhas. Criamos a função da classe Ball, com as seguintes propriedades: raio, cor, posição, velocidade, massa, momento, esfera (com a função sphere) e uma identificação individual para as bolinhas. Agora que criamos o espaço e as bolinhas, precisamos saber se elas colidiram, dessa forma, criamos a função checarColisao, que compara a distancia entre duas bolinhas nos eixos x, y e z. Se as bolinhas estiverem numa distancia menor que o diametro delas (quando comparado com o centro delas), então retorna verdadeiro para a função, se não, falso.

Após isso, fizemos um loop para randomizar as propriedades da classe, e criamos uma variável dt, que controla a velocidade. Na linha seguinte, printamos as bolinhas. Para simular infinitamente o sistema de gases, criamos um loop que não para utilizando While True. Nesse while, verificamos se a função checarColisão é True para 2 bolinhas quaisquer, se for True, então ela inverte as coordenadas em x, y e z nas duas bolas. Analisamos as particle em balls, definimos que as particulas, posição e esfera são iguais a soma das particulas, esfera e posição mais o momento sobre a massa (equivalente a velocidade) vezes o dt, que ajusta a velocidade. 

Logo após, fizemos outro loop para verificar se as bolinhas não estavam entre as bordas das caixas, se fosse verdadeiro, o momento da partícula será invertido para ela retornar para a caixa.

Para descrevermos a velocidade das partículas podemos usar a Distribuição de Maxwell-Boltzmann, que relaciona a velocidade das partículas à sua temperatura, com isso podemos, a partir de algumas deduções descobrir a velocidade média das partículas, a velocidade mais provável de ser encontrada e a velocidade media quadrática, então temos respectivamente:

Equação 1: v =  (8.k.T/m.π)^0.5

Equação 2: v = (2.k.T/m)^0.5

Equação 3: v = (3.k.T/m)^0.5

Cada termo da equação apresenta uma caracteristica das moleculas do gás, sendo k a constante de boltsmann (relaciona a constante dos gases perfeitos com a constante de avogrado), T a temperatura em kelvins e m a massa em gramas.

Inicialmente, o código foi escrito no vscode e salvo com a extenção  .py, sendo possível acessar a simulação pelo cmd com o comando: "py Projeto-bolas.py".
O código está comentado.
A ideia é que agora, apliquemos a distribuição de maxwell boltzmann para as velocidades das partículas.
