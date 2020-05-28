import matplotlib.pyplot as plt

from Random_Walk import RandomWalk

while True :
    
 #Cria um passeio aleatorio e plota os pontos

    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Define o tamanho da janela de plotagem
    
    plt.figure(figsize=(dpi=128,10,6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none',s=1)
    
    #plt.scatter(rw.x_values, rw.y_values, s=15)
    
    # Enfatiza o primeiro e o ultimo ponto
    plt.scatter(0,0, c='green', edgecolors='none',s=45)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red',edgecolors='none',s=45)
    
    #Remove os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show() 

    keep_running = input ("Make another walk? (y/n): ")

    if keep_running == 'n': 
        break