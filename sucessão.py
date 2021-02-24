#Importação do módulo "Math"
import math

#Print inicial
print('Vejo que o Termo Geral da sucessão é 2^(n-1)')

#Input do termo pretendido (un)
un = int(input('Indique o termo do qual quer saber o número de grãos(n): '))

#Cálculo do número de grãos nesse termo (un) da sucessão
numero_graos = 2**(un-1)

#Apresentação do termo ao utilizador
print('À luz do Termo Geral 2^(n-1), temos que, na {}ª casa, o número de grãos recebidos vai ser de {}!'.format(un, numero_graos))

#Definir fecho do programa
input('Para encerrar o programa, carregue ENTER')

#Desenvolvido por Rodrigo Viegas e Daniela Mendes no âmbito da disciplina de Matemática A de 11º ano.