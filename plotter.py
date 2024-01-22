import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# class FileReader:
#     def __init__(self):
#         pass

#     #TODO: add headers: list[str], sep: str
#     def load(file: str):
#         data = pd.read_csv(file)
#         return data


data = pd.read_csv('steam.csv', header=None, names=['game', 'price', 'hasDiscount', 'genres'])

print(data)

data.plot()

plt.show()

#Guido Flores
#Grafico que muestra a los juegos con su respectivo precio
data_to_plot = data[['game', 'price']]

data_to_plot.set_index('game').plot(kind='bar', legend=False)
plt.xlabel('Game')
plt.ylabel('Price')
plt.title('Prices of Games')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()  
plt.show()
