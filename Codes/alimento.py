import pandas as pd

alimentos_db = pd.DataFrame(columns = ['id_alimento', 'alimento', 'gorduras', 'proteínas', 'carboidratos', 'calorias'])

def gerenciar_alimentos(): 
    
  print("Menu de Alimentos\n")
  print("1. Cadastrar\n")
  print("2. Remover\n")
  print("3. Editar\n")
  print("4. Sair\n")

  escolha = input("Digite o número da opção desejada: ")

  if escolha == "1":
    cadastrar_alimento()
  elif escolha == "2":
    remover_alimento()  
  elif escolha == "3":
    return
  else:
    print("Opção inválida. Tente novamente.")

def cadastrar_alimento():
  id_alimento = int(input("ID do paciente: "))
  food = (input('Alimento: '))
  fat = int(input('Gorduras: '))
  protein = int(input('Proteínas: '))
  carbs = int(input('Carboidratos: '))
  calories = int(input('Calorias: '))

  alimentos_db.loc[len(alimentos_db)] = [id_alimento, food, fat, protein, carbs, calories]

def remover_alimento(item):
  for i in range(len(alimentos_db)):
    if alimentos_db.alimento[i] == item:
      alimentos_db = alimentos_db.drop(index)

