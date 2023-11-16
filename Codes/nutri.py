import paciente, alimento

def menu():
  alimento.cadastrar_alimento()

# Cadastro de paciente pelo nutri: 
def cadastro():
  while True:
    paciente.cadastrar_paciente()
    add = input("Adicionar outro paciente (S/N)? ").lower()
    if add != 's':
      break

def gerenciarPlano(paciente):
  if paciente in paciente.pacientes:
    for i in range():
      
# def gerenciarMedidas():

# def login():
