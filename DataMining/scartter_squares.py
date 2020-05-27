import matplotlib.pyplot as plt

x_values=list(range(1,500))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,edgecolors='none', c=y_values,cmap=plt.cm.Blues,s=40)
 
#Define o titulo do grafico e nomeia os eixos
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squere of the Value", fontsize=14)

plt.tick_params(axis='both',which='major', labelsize=14)

#Define o intervalo para cada eixo

plt.axis([0,510,0,130000000])

plt.show()