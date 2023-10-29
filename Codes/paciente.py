
#classe Paciente
class Paciente:
    def __init__(self, nome, peso, altura, idade, sexo, fatoratividade):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.sexo = sexo
        self.fatoratividade = fatoratividade

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

# def consultarPlano:

# def consultarDados:

# def registrarRefeicao: 