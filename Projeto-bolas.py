# Importar bibliotecas do vpython e random
from vpython import *
import random as rand
import time as ti

#definindo n_particulas = 0
n_particulas = 0   
#Criando inputs para o usuário alterar
print("Bem-Vindo(a) ao simulador de colisões entre partícuas de Argônio (Ar)\n")
ti.sleep(1)
print("__________________________________________________________________________\n")
ti.sleep(1)
print("Para iniciar a simulação será necessário que você introduza alguns parâmetros. Vamos lá?!\n")
print("__________________________________________________________________________\n")
print('Recomendações iniciais:\n -Para o número de partículas, recomendamos *50* no máximo, pois mais que essa quantidade a visualização acaba sendo difícil.\n****************************')
n_particulas = int(input("Quantas partículas deseja simular?")) #número de partículas
temperatura = int(input("Qual a temperatura em K (Kelvins) que você deseja simular?")) #valor da temperatura


if n_particulas != 0:

    #Variáveis que definem:
    side = 1000         #Tamanho dos lados sistema
    thk = 0.3           #Espessura da parede
    s2 = 2*side - thk  #Considera o tamanho das paredes junto da espessura delas
    s3 = 2*side + thk  #Considera a altura das paredes junto da espessura delas
    balls = []
    cores = [color.red, color.green]

    #Criação das paredes
    #Parede = cria uma caixa (Cada parede é uma caixa) com os vetores posição 50, 0, 0 e vetores tamanho (espessura, tamanho horizontal, tamanho vertical) e escolhe a cor vermelha
    #Segue o padrão para linha WallR e WallL
    wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
    wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
    #No WallB e WallT a espessura do size vector é em y, e suas dimensões quadráticas estão em x e z
    wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue) #Chão
    wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue) #Teto
    #No WallBk, sua espessura é em z, pois está no fundo, com dimensões de x e y de seu tamanho
    wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7)) #Fundo


    #Criando Bolas com classe, pois otimiza a programação, da pra colocar várias propriedades diferentes e usar uma variável pra todas as bolinhas
    class Ball():  #Cria uma classe Ball (Estrutura que define propriedades de objetos, bolas neste caso)
        def __init__(self, radius, color, pos, velocity, mass, ID): #Função que inicia as propriedades da bola, self, raio, cor, posição, velocidade, massa e ID (identificação de cada bola individualmente)
            self.radius = radius
            self.color = color 
            self.pos = pos
            self.velocity = velocity
            self.mass = mass
            self.p = self.mass*self.velocity
            self.ID = ID
            self.sphere = sphere(mass=self.mass, color=self.color, pos=self.pos, radius=self.radius) #Função da biblioteca

    dt = 0.05 #velocidade da verificação de cada colisão nos frames, calculada a partir de 0.1 da velocidade

    #Checa se colidiu duas bolas diferentes
    def checarColisao(ball1, ball2):
        distanceMax = ((ball2.sphere.pos.x - ball1.sphere.pos.x)**2 + (ball2.sphere.pos.y - ball1.sphere.pos.y)**2 + (ball2.sphere.pos.z - ball1.sphere.pos.z)**2)**(1/2)
        if distanceMax < (ball1.radius+ball2.radius):
            return True
        else:
            return False
        

    for j in range(0, 250): #Função que cria as bolinhas aleatóriamente, faz elas mexerem
        balls.append(Ball(40, rand.choice(cores), vector(rand.randrange(-side, side), rand.randrange(-side, side), rand.randrange(-side, side)), vector(rand.randrange(-100, 100), rand.randrange(-100, 100), rand.randrange(-100, 100)), 40, j))

    while True:
        rate(1000)
        for i in range(0, len(balls)):
            for k in range(i+1, len(balls)):
                if checarColisao(balls[i], balls[k]): # Se checar colisão (Se colidir) for true, então 
                    balls[i].p.x, balls[k].p.x = balls[k].p.x, balls[i].p.x #Inverte k e i em x, y e z
                    balls[i].p.y, balls[k].p.y = balls[k].p.y, balls[i].p.y
                    balls[i].p.z, balls[k].p.z = balls[k].p.z, balls[i].p.z
                
        for particle in balls:
            particle.sphere.pos = particle.sphere.pos + (particle.p/particle.mass)*dt #(particle.p/particle.mass)*dt --> posição
            if not (side > particle.sphere.pos.x > -side):
                particle.p.x = -particle.p.x
            if not (side > particle.sphere.pos.y > -side):
                particle.p.y = -particle.p.y
            if not (side > particle.sphere.pos.z > -side):
                particle.p.z = -particle.p.z
                
    #Maxwell-boltzmann distribution
    #prob = ((m/2*pi*k*T)**(3/2))*4*pi*(v**2)*(e**(-m*(v**2))/2*k*T)
