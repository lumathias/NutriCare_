import paciente
import alimento
import nutri

# Exemplo de uso:
pessoa = Paciente ('dany maos fofas', 76, 1.74, 27, "masculino", 5)

tmb = Paciente.calcular_tmb(pessoa)
tmb_final = fator_atividade(pessoa)
print(f"TMB: {tmb}")
print(f"TMB Final: {tmb_final}") 