# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não

print("1 idoso")
print("2gestante")
print(" 3 cadeirante")
print("4 nenhuam destes")
reposta= int(input ("você é:"))

if ( reposta==1) or (reposta==2) or (reposta==3):
    print ('você tem direito a fila prioritária')
else:
    print('voê não tem direito a fila prioritaria')