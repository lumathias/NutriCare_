import paciente
import alimento
import nutri

# Exemplo de uso:
pessoa = paciente.Paciente ('dany maos fofas', 76, 1.74, 27, "masculino", 5)

tmb = paciente.Paciente.calcular_tmb(pessoa)
tmb_final = paciente.fator_atividade(pessoa)
print(f"TMB: {tmb}")
print(f"TMB Final: {tmb_final}") 