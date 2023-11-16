import pandas as pd

#Data frame Pacientes

pacientes_db = pd.DataFrame(columns=['id_paciente','Nome', 'Idade', 'Gênero', 'Altura', 'Peso', 'Problemas_de_saúde', 'Dieta'])

# Function to add a new patient record
def cadastrar_paciente():
  id_paciente = int(input("ID do paciente: "))
  nome = input("Nome: ")
  idade = int(input("Idade: "))
  genero = input("Gênero: ")
  altura = float(input("Altura (cm): "))
  peso = float(input("Peso (kg): "))
  medical_conditions = input("Problema(s) de saúde: ")
  diet_plan = input("Plano alimentar: ")

  pacientes_db.loc[len(pacientes_db)] = [id_paciente, nome, idade, genero, altura, peso, medical_conditions, diet_plan]


#calcular taxa metabolismo sem fator atividade
def calcular_tmb(Paciente):
  if Paciente.sexo == "masculino":
    result_tmb = (66 + (13.7 * Paciente.peso) + (5 * Paciente.altura) - (6.8 * Paciente.idade))
  elif Paciente.sexo == "feminino":
    result_tmb = (655 + (9.6 * Paciente.peso) + (1.8 * Paciente.altura) - (4.7 * Paciente.idade))
  else:
    print("erro")
    return 0.0  # Retornar um valor padrão em caso de erro
  return result_tmb

#Funcão para calcular  a taxa de metabolismo final
def fator_atividade(Paciente):
  tmb = calcular_tmb(Paciente)
  if Paciente.fatoratividade < 1:
    result_tmb_final = tmb * 1.2
  elif 1 <= Paciente.fatoratividade < 3:
    result_tmb_final = tmb * 1.375
  elif 3 <= Paciente.fatoratividade < 5:
    result_tmb_final = tmb * 1.55
  elif 5 <= Paciente.fatoratividade <= 6:
    result_tmb_final = tmb * 1.725
  else:
    result_tmb_final = tmb * 1.9
  return result_tmb_final

# def consultarPlano(Paciente):
#  if Paciente == True:


# def consultarDados(Paciente):

# def registrarRefeicao(Paciente):
