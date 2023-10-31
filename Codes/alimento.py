import pandas as pd

alimentos = pd.DataFrame()
alimentos.columns = ['Nome', 'Calorias', 'Gorduras', 'Proteínas']

def cadastrar_alimento():
  alimentos['Nome'] = input('Alimento: ')
  alimentos['Calorias'] = input('Calorias: ')
  alimentos['Gordura'] = input('Gorduras: ')
  alimentos['Proteína'] = input('Proteínas: ')

nomes = alimentos['Nome']

def remover_alimento(alimento):
  for itesm in nomes:
    if alimentos.Nome[item] == alimento:
      alimentos = alimentos.drop(item)