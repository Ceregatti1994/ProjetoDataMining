import matplotlib.pyplot as plt

from Random_Walk import RandomWalk

while True :
    
 #Cria um passeio aleatorio e plota os pontos

    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)

    plt.show() 

    keep_running = input ("Make another walk? (y/n): ")

    if keep_running == 'n': 
        break