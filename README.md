<h1> SIMULADOR DE COLISÕES </h1>

<b> Membros do grupo: Eric, Izaque, Alice, Karla. </b>

<li><b>Simulador de colisões:</b></li>
A ideia do projeto do grupo é desenvolver uma simulação de um gás ideal num modelo de física clássica e sem troca de energia com o exterior, temos como objetivo simular as partículas como bolas de bilhar (massa, área...) que interagem entre si colidindo elasticamente e sem simular as interações intermoleculares (como formações de ligações químicas) a princípio.  

Nosso interesse é desenvolver um programa que permita a visualização e demonstração de conceitos termodinâmicos num gás ideal. Sendo ele composto por partículas independentes, não localizadas e indistinguíveis.

O que foi realizado até então:
Simulamos uma situação com 50 partículas em uma caixa, onde elas colidem elasticamente, até então as bibliotecas vphyton e random foram utilizadas para randomizar as propriedades da classe e o vpython para facilitar a otimização da programação. 
Definimos algumas variáveis de dimensão do sistema, definimos duas listas, uma vazia das bolas que serão criadas no final do prgroama e uma de cores para randomizar nas bolinhas. Criamos a função da classe Ball, com as seguintes propriedades: raio, cor, posição, velocidade, massa, momento, esfera (com a função sphere) e uma identificação individual para as bolinhas. Agora que criamos o espaço e as bolinhas, precisamos saber se elas colidiram, dessa forma, criamos a função checarColisao, que compara a distancia entre duas bolinhas nos eixos x, y e z. Se as bolinhas estiverem numa distancia menor que o diametro delas (quando comparado com o centro delas), então retorna verdadeiro para a função, se não, falso.

Após isso, fizemos um loop para randomizar as propriedades da classe, e criamos uma variável dt, que controla a velocidade. Na linha seguinte, printamos as bolinhas. Para simular infinitamente o sistema de gases, criamos um loop que não para utilizando While True. Nesse while, verificamos se a função checarColisão é True para 2 bolinhas quaisquer, se for True, então ela inverte as coordenadas em x, y e z nas duas bolas. Analisamos as particle em balls, definimos que as particulas, posição e esfera são iguais a soma das particulas, esfera e posição mais o momento sobre a massa (equivalente a velocidade) vezes o dt, que ajusta a velocidade. 

Logo após, fizemos outro loop para verificar se as bolinhas não estavam entre as bordas das caixas, se fosse verdadeiro, o momento da partícula será invertido para ela retornar para a caixa.

Analisando agora os parâmetros temperatura e valocidade, dado o nosso sistema fechado e com uma temperatura constante, sabemos que a energia cinética do sistema também será constante. Por outro lado, as partículas desse gás não estarão todas a uma mesma velocidade, por isso usaremos a Distribuição de Maxwell-Boltzmann para descrevê-las, relacionando quantidade de partículas à determinada velocidade, em uma dada temperatura. 
Com isso podemos, a partir de algumas deduções descobrir a velocidade média das partículas, a velocidade mais provável de ser encontrada e a velocidade media quadrática, então temos respectivamente:

<li><b> Equação 1: v =  (8.k.T/m.π)^0.5 </b></li>
<li><b> Equação 2: v = (2.k.T/m)^0.5 </b></li>
<li><b> Equação 3: v = (3.k.T/m)^0.5 </b></li>

Cada termo da equação apresenta uma caracteristica das moleculas do gás, sendo k a constante de boltsmann (relaciona a constante dos gases perfeitos com a constante de avogrado), T a temperatura em kelvins e m a massa em gramas.

Inicialmente, o código foi escrito no vscode e salvo com a extenção  .py, sendo possível acessar a simulação pelo cmd com o comando: "py Projeto-bolas.py".
O código está comentado.
A ideia é que agora, apliquemos a distribuição de maxwell boltzmann para as velocidades das partículas.


A distribuição de maxwell boltzmann para as velocidades das partículas ainda não foi implementada no código, estando em processo de estudo. Essa distribuição possibilita observar a velocidade das partículas, em uma distribuição probabilística, em determinada temperatura, comprovando seu comportamento. Iremos implementar algumas modificações: o usuário poderá alterar a quantidade de partículas e a temperatura da simulação. Além disso, após a sugestão do professor, definimos que o gás  a ser analisado na colisão será o Argônio, sendo composto de partículas  monoatômicas, permitindo que com algumas aproximações seu formato seja bem representado por uma esfera. 

Falamos com o professor Felipe sobre a distribuição de maxwell boltzman, ele nos auxiliou em como deveríamos proceder para fazer a distribuição da velocidade de forma que essa distribuição de boltzman seja satisfeita. No geral, ainda implementaremos a distribuição das velocidades para as partículas e, também, a entrada de temperatura e quantidade de partículas. Além disso começamos a esboçar os gráficos dessa distribuição.

<h2>Para alterar os parâmetros: </h2>
<li> Tamanho da caixa: side, na linha 7 </li>
<li> Espessura das paredes: thk, linha 8 </li>
<li> Cores das bolas: cores, linha 12 </li>
<li> Quantidade de bolas: for j in range(0,x), altere x, linha 50 </li>
<li> Raio: balls.append(Ball(x, ...), altere x, linha 51 </li>
<li> Massa: balls.append(Ball(..., y, j)), altere y, linha 51 </li>
<li> Velocidade: 3 vetores, linha 51 (São os 3 últimos "vector(rand.randrange(-x, x))" da linha) </li>
<li> Velocidade de propagação das bolinhas na simulação: dt, linha 52 (Recomendável utilizar 0.05) </li>
<li> Velocidade dos frames: Rate(x), altere x, 55 (Recomendável utilizar 200, ou mais) </li>



Temos alguns problemas notados:

Em algumas vezes que roda o programa, algumas bolas iniciam fora da caixa

Em algumas vezes que roda o programa, algumas bolas iniciam juntas (como uma ligação química), mas logo depois se desfazem

Reeditar dt para calcular, e não definir, como: dt = 0,1/vel_bolinhas (0,1 equivale a 1% do tamanho de uma caixa com 10 metros)


<li>Nenhum produto encontrado.</li>





<li>Nenhum produto encontrado.</li>
