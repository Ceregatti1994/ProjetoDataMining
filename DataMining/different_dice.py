from die import Die
import pygal 

#Cria dois dados D6

num_times = 50000

die_1 = Die()
die_2 = Die(6)

#Faz alguns lançamentos e armazena os resultados em uma lista

results=[]

for roll_num in range(num_times):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualiza os resultados    
hist = pygal.Bar()

hist.title = "Results of rolling a D" +str(die_1.num_sides) + " and a D" +str(die_2.num_sides) +" "+str(num_times) + " times"
hist.x_labels = list(range(2,max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6' + '10',frequencies)
hist.render_to_file('die_visual.svg')

print("ok")
