import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Obtem as datas e as temperaturas máximas e mínimas do arquivo
filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates,highs, lows = [], [], []
    for row in reader:
        try:
            currente_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(currente_date,'Missing data')
        else:        
            dates.append(currente_date)
            highs.append(high)
            lows.append(low)
        
#Faz a plotagem dos dados

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs, c='red',alpha=0.5)
plt.plot(dates,lows, c='Blue',alpha=0.5)
plt.fill_between(dates,highs,lows, facecolor='Blue', alpha=0.1)

#Formata o gráfico

plt.title("Daily high and low temperatures,2018\n Death Valley", fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params( axis='both', which='major', labelsize=16)

plt.show()
    
   